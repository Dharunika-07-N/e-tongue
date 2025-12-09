from typing import List

from pydantic import BaseModel, Field


class AnalysisRequest(BaseModel):
    sensor_data: List[float] = Field(
        ..., description="Flat list of e-tongue sensor readings (taste channels)."
    )


class AnalysisResponse(BaseModel):
    success: bool
    is_adulterated: bool
    confidence: float
    details: str

