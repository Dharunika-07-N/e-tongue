import uuid
from fastapi import APIRouter, UploadFile, File, Depends, Body
from sqlalchemy.orm import Session

from app.schemas.infer import ImageUploadResponse
from app.schemas.sensor import SensorIn, SensorAck
from app.services.image_processor import process_image_and_predict
from app.services.ingest import ingest_sensor_batch
from app.db.session import get_db

router = APIRouter()


@router.post("/ingest", response_model=SensorAck)
def ingest(sensor_batch: SensorIn = Body(...), db: Session = Depends(get_db)):
    """Ingest a batch of e-tongue sensor values."""
    ingest_sensor_batch(sensor_batch, db)
    return SensorAck(status="ok")


@router.post("/upload_image", response_model=ImageUploadResponse)
async def upload_image(file: UploadFile = File(...), db: Session = Depends(get_db)):
    """Upload an image from Tinkercad, extract sensor values via OCR, and predict adulteration."""
    sensor_id = f"tinkercad-{uuid.uuid4().hex[:8]}"
    return await process_image_and_predict(file, sensor_id, db)


@router.get("/mock", response_model=SensorIn)
def mock_feed():
    """Provide mock sensor data for UI development."""
    return SensorIn(sensor_id="mock-01", values=[123, 256, 301, 220, 180, 90])
    
