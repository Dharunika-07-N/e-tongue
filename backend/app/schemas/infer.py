from typing import List, Optional
from pydantic import BaseModel, Field


class SensorBlock(BaseModel):
    values: List[float] = Field(..., description="Taste sensor channels")


class InferRequest(BaseModel):
    sensor: SensorBlock
    spectra: List[float] = Field(..., description="Flattened spectral vector")
    herb_name: Optional[str] = None
    batch_no: Optional[str] = None
    supplier: Optional[str] = None


class Prediction(BaseModel):
    label: str
    confidence: float


class InferResponse(BaseModel):
    rasa: Prediction
    quality: Prediction
    adulteration: Prediction
    adulteration_score: float
    threshold: float

