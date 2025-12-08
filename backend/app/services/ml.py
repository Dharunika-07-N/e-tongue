import joblib
import numpy as np
from pathlib import Path
from sqlalchemy.orm import Session

from app.schemas.infer import InferRequest, InferResponse, Prediction
from app.services.preprocess import preprocess_sample
from app.core.config import settings


def _load_model(name: str):
    path = Path(settings.MODEL_DIR) / f"{name}.pkl"
    if path.exists():
        return joblib.load(path)
    return None


rasa_model = _load_model("rasa")
quality_model = _load_model("quality")
anomaly_model = _load_model("anomaly")
threshold_model = _load_model("threshold")


def run_inference(req: InferRequest, db: Session) -> InferResponse:
    """Run inference using loaded models and return structured predictions."""
    X = preprocess_sample(req)

    rasa_probs = rasa_model.predict_proba(X)[0] if rasa_model else [0.5, 0.5]
    quality_probs = quality_model.predict_proba(X)[0] if quality_model else [0.5, 0.5]
    adulteration_score = float(anomaly_model.decision_function(X)[0]) if anomaly_model else 0.0
    threshold_pred = float(threshold_model.predict(X)[0]) if threshold_model else 0.0

    rasa_idx = int(np.argmax(rasa_probs))
    quality_idx = int(np.argmax(quality_probs))
    rasa_label = getattr(rasa_model, "classes_", ["unknown"])[rasa_idx] if rasa_model else "unknown"
    quality_label = getattr(quality_model, "classes_", ["authentic"])[quality_idx] if quality_model else "authentic"

    return InferResponse(
        rasa=Prediction(label=str(rasa_label), confidence=float(np.max(rasa_probs))),
        quality=Prediction(label=str(quality_label), confidence=float(np.max(quality_probs))),
        adulteration_score=adulteration_score,
        threshold=threshold_pred,
    )


def model_status():
    return {
        "rasa": bool(rasa_model),
        "quality": bool(quality_model),
        "anomaly": bool(anomaly_model),
        "threshold": bool(threshold_model),
    }


def trigger_retrain():
    # Placeholder hook for background job/worker
    return True

