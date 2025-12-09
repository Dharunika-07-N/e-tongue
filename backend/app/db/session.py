import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

logger = logging.getLogger(__name__)

db_url = settings.DATABASE_URL
if not db_url:
    raise RuntimeError("DATABASE_URL is not set. Set the env var or provide a .env file.")

connect_args = {}
if db_url.lower().startswith("sqlite"):
    connect_args = {"check_same_thread": False}

try:
    engine = create_engine(db_url, connect_args=connect_args)
except Exception as exc:
    logger.exception("Failed to create DB engine for '%s': %s", db_url, exc)
    raise

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """FastAPI dependency to provide a DB session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()