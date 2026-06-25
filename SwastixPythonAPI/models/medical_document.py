from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.sql import func
from database import Base
import enum


class DocumentType(str, enum.Enum):
    """Type of medical documents"""
    PRESCRIPTION = "prescription"
    DIAGNOSIS_REPORT = "diagnosis_report"
    EXAM_REPORT = "exam_report"
    LAB_REPORT = "lab_report"
    MEDICAL_CERTIFICATE = "medical_certificate"
    OTHER = "other"


class MedicalDocument(Base):
    """Medical documents (prescriptions, diagnosis reports, etc.)"""
    __tablename__ = "medical_documents"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False, index=True)
    appointment_id = Column(Integer, ForeignKey("appointments.id"), nullable=True, index=True)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=True, index=True)

    # Document Details
    document_type = Column(Enum(DocumentType), nullable=False, index=True)
    document_url = Column(String(500), nullable=False)
    file_name = Column(String(255), nullable=False)
    description = Column(String(500), nullable=True)

    # Metadata
    uploaded_by_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # User who uploaded

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<MedicalDocument(id={self.id}, type={self.document_type}, patient_id={self.patient_id})>"
