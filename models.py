"""Database models for Asset Audit system."""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Asset(Base):
    """Asset audit record."""
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    sl_no = Column(Integer, unique=True, nullable=False, index=True)
    asset_name = Column(String(255), nullable=False, index=True)
    dop = Column(String(20))  # DD/MM/YYYY format
    quantity = Column(Integer, default=1)
    si_no = Column(String(255), index=True)
    age = Column(String(50))
    disposed = Column(Boolean, default=False)
    disposal_date = Column(String(20))
    disposal_reason = Column(String(255))
    vendor = Column(String(255), index=True)
    value = Column(Float)  # Total value (base + GST if applicable)
    base_price = Column(Float)  # Base price before GST
    gst_applicable = Column(Boolean, default=False)  # Whether GST was paid
    gst_mode = Column(String(20), default="percent")  # percent or amount
    gst_place = Column(String(20), default="intra")  # intra or inter
    gst_rate = Column(Float, default=0)  # GST rate (5, 12, 18, 28)
    gst_amount = Column(Float, default=0)  # Calculated GST amount
    cgst_rate = Column(Float, default=0)
    sgst_rate = Column(Float, default=0)
    igst_rate = Column(Float, default=0)
    cgst_amount = Column(Float, default=0)
    sgst_amount = Column(Float, default=0)
    igst_amount = Column(Float, default=0)
    location = Column(String(255), index=True)
    purchased_from = Column(String(255), index=True)
    department = Column(String(255), index=True)
    asset_type = Column(String(100), index=True)  # Laptop, Tab, Desktop, etc.
    status = Column(String(50), default="Functional", index=True)  # Functional, Non-Functional, Condemned
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    class Config:
        from_attributes = True


class MaintenanceLog(Base):
    """Maintenance log entry for assets."""
    __tablename__ = "maintenance_logs"

    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(Integer, nullable=False, index=True)
    entry_type = Column(String(50), nullable=False)  # Repair, Inspection, Scheduled, Discarded
    date = Column(String(20), nullable=False)  # DD/MM/YYYY format
    technician = Column(String(255), nullable=False)
    notes = Column(String(1000))
    cost = Column(Float, default=0)
    scrap_value = Column(Float, default=0)  # Scrap/disposal value for discarded items
    status = Column(String(50), nullable=False)  # Pending, In Progress, Completed
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    class Config:
        from_attributes = True
