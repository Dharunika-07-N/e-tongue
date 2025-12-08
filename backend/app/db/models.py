from sqlalchemy import Column, Integer, String, JSON, Float, DateTime
from sqlalchemy.sql import func

from app.db.session import Base


class Sample(Base):
    __tablename__ = "samples"

    id = Column(Integer, primary_key=True, index=True)
    herb_name = Column(String, index=True)
    batch_no = Column(String, index=True)
    supplier = Column(String)
    sensor = Column(JSON)
    spectra = Column(JSON)
    rasa = Column(String)
    rasa_conf = Column(Float)
    quality = Column(String)
    quality_conf = Column(Float)
    adulteration_score = Column(Float)
    threshold_pred = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Calibration(Base):
    __tablename__ = "calibrations"

    id = Column(Integer, primary_key=True, index=True)
    sensor_id = Column(String, index=True)
    offset = Column(Float)
    gain = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

