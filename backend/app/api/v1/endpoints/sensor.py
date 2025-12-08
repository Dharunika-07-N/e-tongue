from fastapi import APIRouter, Body, Depends
from sqlalchemy.orm import Session

from app.schemas.sensor import SensorIn, SensorAck
from app.services.ingest import ingest_sensor_batch
from app.db.session import get_db

router = APIRouter()


@router.post("/ingest", response_model=SensorAck)
def ingest(sensor_batch: SensorIn = Body(...), db: Session = Depends(get_db)):
    """Ingest a batch of e-tongue sensor values."""
    ingest_sensor_batch(sensor_batch, db)
    return SensorAck(status="ok")


@router.get("/mock", response_model=SensorIn)
def mock_feed():
    """Provide mock sensor data for UI development."""
    return SensorIn(sensor_id="mock-01", values=[123, 256, 301, 220, 180, 90])

