from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.routes import api_router
from app.core.config import settings
from app.db.session import Base, engine


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
    )

    app.include_router(api_router, prefix="/api/v1")

    return app

app = create_app()


@app.get("/health")
def health():
    return {"status": "ok"}
