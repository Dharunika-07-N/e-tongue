from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session

from app.services.ingest import ingest_spectra_file
from app.db.session import get_db

router = APIRouter()


@router.post("/upload")
async def upload_spectra(
    herb_name: str = Form(...),
    batch_no: str = Form(...),
    supplier: str = Form(""),
    spectra_type: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    """Upload spectral file (FTIR/NIR/Raman/HPTLC/LC-MS) with metadata."""
    await ingest_spectra_file(
        file=file,
        herb_name=herb_name,
        batch_no=batch_no,
        supplier=supplier,
        spectra_type=spectra_type,
        db=db,
    )
    return {"status": "ok"}

