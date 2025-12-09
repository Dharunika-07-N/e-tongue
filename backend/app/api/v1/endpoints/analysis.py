import logging
from fastapi import APIRouter

from app.schemas.analysis import AnalysisRequest, AnalysisResponse
from app.services.adulteration import analyze_sensor_vector

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/adulteration", response_model=AnalysisResponse)
def analyze_adulteration(req: AnalysisRequest):
    """
    Lightweight adulteration-only analysis endpoint.

    Returns a mock response when the model artifact is missing so the frontend
    can still be demoed without a trained model.
    """
    is_adulterated, confidence, details = analyze_sensor_vector(req.sensor_data)
    logger.info(
        "Adulteration analysis completed is_adulterated=%s confidence=%.3f",
        is_adulterated,
        confidence,
    )
    return AnalysisResponse(
        success=True,
        is_adulterated=is_adulterated,
        confidence=confidence,
        details=details,
    )

