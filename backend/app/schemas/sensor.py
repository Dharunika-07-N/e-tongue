from typing import List
from pydantic import BaseModel, Field


class SensorIn(BaseModel):
    sensor_id: str = Field(..., description="Unique sensor module ID")
    values: List[float] = Field(..., description="Array of taste channel readings")


class SensorAck(BaseModel):
    status: str

