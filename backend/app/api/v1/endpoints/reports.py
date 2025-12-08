from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.services.report import build_report

router = APIRouter()


@router.get("/{sample_id}")
def get_report(sample_id: int):
    """Generate and return PDF report for a sample."""
    pdf_path = build_report(sample_id)
    return FileResponse(pdf_path, media_type="application/pdf", filename=f"sample-{sample_id}.pdf")

