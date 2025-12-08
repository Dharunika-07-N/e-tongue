from pydantic import Field
from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    APP_NAME: str = "E-Tongue Herbal QA"
    API_PREFIX: str = "/api/v1"
    ALLOW_ORIGINS: List[str] = Field(default_factory=lambda: ["*"])
    DATABASE_URL: str = "sqlite:///./e_tongue.db"  # replace with Postgres in prod
    MODEL_DIR: str = "models"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

