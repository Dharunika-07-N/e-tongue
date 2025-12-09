import joblib
import numpy as np
from pathlib import Path
from sqlalchemy.orm import Session

from app.schemas.infer import InferRequest, InferResponse, Prediction
from app.services.preprocess import preprocess_sample
from app.core.config import settings

# Global cache for lazy-loaded models
_models_cache = {}

def _load_model(name: str):
    """Load model from disk (cached after first load)."""
    if name in _models_cache:
        return _models_cache[name]
    
    path = Path(settings.MODEL_DIR) / f"{name}.pkl"
    try:
        if path.exists():
            model = joblib.load(path)
            _models_cache[name] = model
            return model
    except Exception as e:
        print(f"Warning: Failed to load model {name} from {path}: {e}")
    
    _models_cache[name] = None
    return None

def _get_models():
    """Get all models (lazy load)."""
    return {
        "rasa": _load_model("rasa"),
        "quality": _load_model("quality"),
        "anomaly": _load_model("anomaly"),
        "threshold": _load_model("threshold"),
        "adulteration": _load_model("adulteration"),
    }

def run_inference(req: InferRequest, db: Session) -> InferResponse:
    """Run inference using loaded models and return structured predictions."""
    models = _get_models()
    rasa_model = models["rasa"]
    quality_model = models["quality"]
    anomaly_model = models["anomaly"]
    threshold_model = models["threshold"]
    adulteration_model = models["adulteration"]
    
    X = preprocess_sample(req)
    sensor_features = np.array(req.sensor.values, dtype=float).reshape(1, -1)

    rasa_probs = rasa_model.predict_proba(X)[0] if rasa_model else [0.5, 0.5]
    quality_probs = quality_model.predict_proba(X)[0] if quality_model else [0.5, 0.5]
    adulteration_score = float(anomaly_model.decision_function(X)[0]) if anomaly_model else 0.0
    threshold_pred = float(threshold_model.predict(X)[0]) if threshold_model else 0.0
    adulteration_probs = (
        adulteration_model.predict_proba(sensor_features)[0]
        if adulteration_model
        else [0.5, 0.5]
    )

    rasa_idx = int(np.argmax(rasa_probs))
    quality_idx = int(np.argmax(quality_probs))
    adulteration_idx = int(np.argmax(adulteration_probs))
    rasa_label = getattr(rasa_model, "classes_", ["unknown"])[rasa_idx] if rasa_model else "unknown"
    quality_label = getattr(quality_model, "classes_", ["authentic"])[quality_idx] if quality_model else "authentic"
    adulteration_label = (
        getattr(adulteration_model, "classes_", ["Adulterated", "Pure"])[adulteration_idx]
        if adulteration_model
        else "Unknown"
    )

    return InferResponse(
        rasa=Prediction(label=str(rasa_label), confidence=float(np.max(rasa_probs))),
        quality=Prediction(label=str(quality_label), confidence=float(np.max(quality_probs))),
        adulteration=Prediction(
            label=str(adulteration_label), confidence=float(np.max(adulteration_probs))
        ),
        adulteration_score=adulteration_score,
        threshold=threshold_pred,
    )


def model_status():
    """Return model availability status."""
    models = _get_models()
    return {
        "rasa": bool(models["rasa"]),
        "quality": bool(models["quality"]),
        "anomaly": bool(models["anomaly"]),
        "threshold": bool(models["threshold"]),
        "adulteration": bool(models["adulteration"]),
    }


def trigger_retrain():
    """Placeholder hook for background job/worker."""
    return True
