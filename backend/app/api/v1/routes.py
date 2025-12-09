from fastapi import APIRouter

from app.api.v1.endpoints import analysis, sensor, infer, spectra, models, reports

api_router = APIRouter()

api_router.include_router(sensor.router, prefix="/sensor", tags=["sensor"])
api_router.include_router(spectra.router, prefix="/spectra", tags=["spectra"])
api_router.include_router(infer.router, prefix="/infer", tags=["inference"])
api_router.include_router(models.router, prefix="/models", tags=["models"])
api_router.include_router(reports.router, prefix="/reports", tags=["reports"])
api_router.include_router(analysis.router, prefix="/analysis", tags=["analysis"])

