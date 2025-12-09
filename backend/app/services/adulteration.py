import logging
from pathlib import Path
from typing import List, Tuple

import joblib
import numpy as np
from fastapi import HTTPException

from app.core.config import settings

logger = logging.getLogger(__name__)
_adulteration_model = None


def _load_adulteration_model():
    """
    Lazy-load the adulteration model from disk.

    Returns None when the artifact is missing or fails to load so callers can
    decide whether to return a mock response or raise a clear error.
    """
    global _adulteration_model
    if _adulteration_model is not None:
        return _adulteration_model

    model_path = Path(settings.MODEL_DIR) / "adulteration.pkl"
    if not model_path.exists():
        logger.warning("Adulteration model not found at %s", model_path)
        _adulteration_model = None
        return _adulteration_model

    try:
        _adulteration_model = joblib.load(model_path)
        logger.info("Adulteration model loaded from %s", model_path)
    except Exception as exc:  # pragma: no cover - defensive guard
        logger.exception("Failed to load adulteration model: %s", exc)
        _adulteration_model = None
    return _adulteration_model


def _prep_vector(sensor_data: List[float]) -> np.ndarray:
    """Validate and reshape the incoming sensor vector."""
    try:
        arr = np.array(sensor_data, dtype=float).reshape(1, -1)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Invalid sensor_data: {exc}") from exc

    if arr.size == 0:
        raise HTTPException(status_code=400, detail="sensor_data cannot be empty")

    if not np.isfinite(arr).all():
        raise HTTPException(status_code=400, detail="sensor_data must be finite numeric values")

    return arr


def analyze_sensor_vector(sensor_data: List[float]) -> Tuple[bool, float, str]:
    """
    Run adulteration analysis using the trained model.

    Returns a tuple of (is_adulterated, confidence, detail_message).
    Provides a deterministic mock response when no model is available so the
    UI remains usable during demo/testing.
    """
    vector = _prep_vector(sensor_data)
    model = _load_adulteration_model()

    if model is None:
        logger.warning("Adulteration model unavailable; returning mock response.")
        return False, 0.85, "Mock analysis - model not yet trained"

    try:
        prediction = model.predict(vector)[0]
        has_proba = hasattr(model, "predict_proba")
        probas = model.predict_proba(vector)[0] if has_proba else [0.5, 0.5]
        # Assume label "Adulterated" corresponds to positive class when available.
        positive_idx = 1 if len(probas) > 1 else 0
        confidence = float(probas[positive_idx])
        is_adulterated = str(prediction).lower() != "pure"
        detail = "Analysis completed successfully"
        logger.debug("Adulteration prediction=%s confidence=%.4f", is_adulterated, confidence)
        return is_adulterated, confidence, detail
    except HTTPException:
        raise
    except Exception as exc:  # pragma: no cover - runtime safety
        logger.exception("Adulteration analysis failed: %s", exc)
        raise HTTPException(status_code=500, detail=f"Analysis failed: {exc}") from exc

