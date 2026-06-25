from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base


class Prescription(Base):
    """Prescriptions created by doctors"""
    __tablename__ = "prescriptions"

    id = Column(Integer, primary_key=True, index=True)
    appointment_id = Column(Integer, ForeignKey("appointments.id"), nullable=False, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False, index=True)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False, index=True)

    # Medicine Details (can be stored as JSON for multiple medicines)
    medicine_name = Column(String(255), nullable=False)
    dosage = Column(String(100), nullable=False)  # e.g., "500mg"
    frequency = Column(String(100), nullable=False)  # e.g., "twice daily"
    duration = Column(String(100), nullable=False)  # e.g., "7 days"
    instructions = Column(Text, nullable=True)

    # Additional Info
    is_active = Column(String(50), default=True)
    notes = Column(Text, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<Prescription(id={self.id}, appointment_id={self.appointment_id}, medicine={self.medicine_name})>"
