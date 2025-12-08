import json
from pathlib import Path
from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.db import models


def ingest_sensor_batch(sensor_batch, db: Session):
    """Persist raw sensor values."""
    sample = models.Sample(
        herb_name=None,
        batch_no=None,
        supplier=None,
        sensor=sensor_batch.dict(),
    )
    db.add(sample)
    db.commit()
    db.refresh(sample)
    return sample.id


async def ingest_spectra_file(file: UploadFile, herb_name: str, batch_no: str, supplier: str, spectra_type: str, db: Session):
    """Store spectral file path reference; saves file to data directory."""
    data_dir = Path("data") / "uploads"
    data_dir.mkdir(parents=True, exist_ok=True)
    dest = data_dir / f"{batch_no}-{spectra_type}-{file.filename}"
    content = await file.read()
    dest.write_bytes(content)

    upload = models.Sample(
        herb_name=herb_name,
        batch_no=batch_no,
        supplier=supplier,
        spectra={"type": spectra_type, "path": str(dest)},
    )
    db.add(upload)
    db.commit()
    db.refresh(upload)
    return upload.id

