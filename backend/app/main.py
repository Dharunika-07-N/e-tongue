import logging
from contextlib import asynccontextmanager
from typing import Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.routes import api_router
from app.core.config import settings
from app.db.session import Base, engine
from app.schemas.analysis import AnalysisRequest
from app.services.adulteration import analyze_sensor_vector, _load_adulteration_model

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Ensure tables exist for SQLite demo; replace with migrations in prod."""
    try:
        Base.metadata.create_all(bind=engine)
        print("Database tables created/verified successfully")
    except Exception as exc:
        import logging
        logger = logging.getLogger("uvicorn.error")
        logger.exception("Database initialization failed: %s", exc)
        raise
    yield


def create_app() -> FastAPI:
    
    app = FastAPI(title="E-Tongue Herbal QA", version="1.0.0", lifespan=lifespan)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOW_ORIGINS,
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
        expose_headers=["*"],
    )

    app.include_router(api_router, prefix="/api/v1")

    return app

app = create_app()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/api/health")
def api_health() -> Dict[str, object]:
    """Health endpoint that also reports model availability."""
    model_loaded = _load_adulteration_model() is not None
    return {"status": "ok", "model_loaded": model_loaded}


@app.get("/api/test-analysis")
def api_test_analysis() -> Dict[str, object]:
    """Run a deterministic mock analysis for quick manual testing."""
    dummy = AnalysisRequest(sensor_data=[0.82, 0.31, 0.15, 0.93, 0.41, 0.54])
    is_adulterated, confidence, details = analyze_sensor_vector(dummy.sensor_data)
    return {
        "success": True,
        "is_adulterated": is_adulterated,
        "confidence": confidence,
        "details": details,
        "sample": dummy.sensor_data,
    }
