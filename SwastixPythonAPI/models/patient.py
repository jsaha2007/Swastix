from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class Patient(Base):
    """Patient model"""
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False, index=True)

    # Personal Information
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    date_of_birth = Column(DateTime(timezone=True), nullable=True)
    gender = Column(String(20), nullable=True)  # Male, Female, Other

    # Contact Information
    address = Column(Text, nullable=True)
    city = Column(String(100), nullable=True, index=True)
    state = Column(String(100), nullable=True)
    postal_code = Column(String(20), nullable=True)

    # Medical Information
    medical_history = Column(Text, nullable=True)  # Free text or JSON
    allergies = Column(Text, nullable=True)
    blood_group = Column(String(10), nullable=True)

    # Communication Preferences
    consent_sms = Column(Boolean, default=True)
    consent_email = Column(Boolean, default=True)

    # Profile
    profile_picture_url = Column(String(500), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<Patient(id={self.id}, name={self.first_name} {self.last_name})>"
