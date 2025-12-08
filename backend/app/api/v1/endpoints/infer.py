from fastapi import APIRouter, Body, Depends
from sqlalchemy.orm import Session

from app.schemas.infer import InferRequest, InferResponse
from app.services.ml import run_inference
from app.db.session import get_db

router = APIRouter()


@router.post("/", response_model=InferResponse)
def infer(req: InferRequest = Body(...), db: Session = Depends(get_db)):
    """Run inference on combined sensor + spectral data."""
    return run_inference(req, db)

