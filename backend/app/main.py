from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.routes import api_router
from app.core.config import settings


def create_app() -> FastAPI:
    """Create FastAPI application with CORS and route registration."""
    app = FastAPI(title="E-Tongue Herbal QA", version="1.0.0")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOW_ORIGINS,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router, prefix="/api/v1")
    return app


app = create_app()


@app.get("/health")
def health():
    return {"status": "ok"}

