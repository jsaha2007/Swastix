from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
import enum


class DoctorSpecialty(str, enum.Enum):
    """Doctor specializations"""
    GENERAL = "general"
    CARDIOLOGY = "cardiology"
    DERMATOLOGY = "dermatology"
    ORTHOPEDICS = "orthopedics"
    PEDIATRICS = "pediatrics"
    NEUROLOGY = "neurology"
    PSYCHIATRY = "psychiatry"
    ENT = "ent"
    OPHTHALMOLOGY = "ophthalmology"
    GYNECOLOGY = "gynecology"
    OTHER = "other"


class Doctor(Base):
    """Doctor model"""
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False, index=True)

    # Personal Information
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    date_of_birth = Column(DateTime(timezone=True), nullable=True)
    gender = Column(String(20), nullable=True)

    # Professional Information
    specialization = Column(Enum(DoctorSpecialty), nullable=False, index=True)
    qualification = Column(Text, nullable=True)  # Degrees, certifications (can be JSON)
    license_number = Column(String(100), nullable=True, unique=True)
    years_of_experience = Column(Integer, nullable=True)
    bio = Column(Text, nullable=True)

    # Contact Information
    address = Column(Text, nullable=True)
    city = Column(String(100), nullable=True, index=True)
    state = Column(String(100), nullable=True)
    postal_code = Column(String(20), nullable=True)

    # Consultation Details
    consultation_fee = Column(Float, nullable=False)  # In INR
    consultation_duration_minutes = Column(Integer, default=30)

    # Profile
    profile_picture_url = Column(String(500), nullable=True)
    resume_url = Column(String(500), nullable=True)

    # Status
    is_approved = Column(Boolean, default=False, index=True)
    is_active = Column(Boolean, default=True, index=True)
    rejection_reason = Column(Text, nullable=True)

    # Ratings
    average_rating = Column(Float, default=0.0)
    total_ratings = Column(Integer, default=0)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<Doctor(id={self.id}, name={self.first_name} {self.last_name}, specialty={self.specialization})>"
