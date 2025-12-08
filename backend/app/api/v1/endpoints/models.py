from fastapi import APIRouter

from app.services.ml import model_status, trigger_retrain

router = APIRouter()


@router.get("/status")
def status():
    """Return currently loaded model info."""
    return model_status()


@router.post("/retrain")
def retrain():
    """Trigger background retraining (mock trigger)."""
    trigger_retrain()
    return {"status": "queued"}

