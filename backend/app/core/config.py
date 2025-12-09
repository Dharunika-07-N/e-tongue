from pathlib import Path
import os
from typing import List

# Try to import BaseSettings in a way that works across environments
try:
    from pydantic_settings import BaseSettings
    from pydantic import Field, ConfigDict
except Exception:
    from pydantic import BaseSettings, Field, ConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_DB = f"sqlite:///{BASE_DIR / 'e_tongue.db'}"


class Settings(BaseSettings):
    APP_NAME: str = "E-Tongue Herbal QA"
    API_PREFIX: str = "/api/v1"
    ALLOW_ORIGINS: List[str] = Field(
        default_factory=lambda: [
            "http://localhost:5173",
            "http://localhost:3000",
            "http://127.0.0.1:5173",
            "http://127.0.0.1:3000",
            "*"
        ]
    )
    # Prefer explicit env var DATABASE_URL, otherwise use project-local sqlite DB
    DATABASE_URL: str = Field(default_factory=lambda: os.getenv("DATABASE_URL", DEFAULT_DB))
    MODEL_DIR: str = "models"

    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


settings = Settings()