from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def build_report(sample_id: int) -> str:
    """Generate a simple PDF report placeholder."""
    reports_dir = Path("data") / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    pdf_path = reports_dir / f"sample-{sample_id}.pdf"

    c = canvas.Canvas(str(pdf_path), pagesize=A4)
    c.drawString(72, 800, f"E-Tongue Herbal QA Report #{sample_id}")
    c.drawString(72, 780, "Predictions and spectra summaries will appear here.")
    c.showPage()
    c.save()
    return str(pdf_path)

