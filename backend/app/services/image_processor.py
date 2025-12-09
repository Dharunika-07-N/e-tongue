from pathlib import Path
from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.schemas.infer import ImageUploadResponse
from app.schemas.sensor import SensorIn
from app.services.ingest import ingest_sensor_batch


async def process_image_and_predict(file: UploadFile, sensor_id: str, db: Session) -> ImageUploadResponse:
    """
    Store uploaded image and ingest a placeholder sensor batch.

    Real OCR is out of scope for this scaffold; we persist the image for future
    processing and record a dummy sensor payload so downstream flows keep
    working end-to-end.
    """
    uploads_dir = Path("data") / "uploads"
    uploads_dir.mkdir(parents=True, exist_ok=True)
    dest = uploads_dir / f"{sensor_id}-{file.filename}"

    content = await file.read()
    dest.write_bytes(content)

    # Placeholder sensor values so downstream inference stays functional.
    placeholder_values = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    ingest_sensor_batch(SensorIn(sensor_id=sensor_id, values=placeholder_values), db)

    return ImageUploadResponse(
        success=True,
        message="Image stored for processing; OCR placeholder values recorded.",
        file_path=str(dest),
    )

