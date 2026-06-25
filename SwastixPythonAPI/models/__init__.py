from sqlalchemy import Column, Integer, String, Enum, DateTime, Boolean
from sqlalchemy.sql import func
from database import Base
import enum
from datetime import datetime


class RoleEnum(str, enum.Enum):
    """User roles"""
    PATIENT = "patient"
    DOCTOR = "doctor"
    ADMIN = "admin"


class User(Base):
    """Base User model for all roles"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    phone = Column(String(20), unique=True, index=True, nullable=False)
    role = Column(Enum(RoleEnum), nullable=False, index=True)
    is_active = Column(Boolean, default=True, index=True)
    is_verified = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email}, role={self.role})>"


# Import all other models
from .otp import OTP
from .patient import Patient
from .doctor import Doctor, DoctorSpecialty
from .timeslot import Timeslot, DayOfWeek, TimeslotStatus
from .appointment import Appointment, ConsultationType, AppointmentStatus
from .medical_document import MedicalDocument, DocumentType
from .rating import Rating
from .prescription import Prescription
from .admin import Admin
from .notification import Notification, NotificationType, NotificationChannel

__all__ = [
    "User",
    "RoleEnum",
    "OTP",
    "Patient",
    "Doctor",
    "DoctorSpecialty",
    "Timeslot",
    "DayOfWeek",
    "TimeslotStatus",
    "Appointment",
    "ConsultationType",
    "AppointmentStatus",
    "MedicalDocument",
    "DocumentType",
    "Rating",
    "Prescription",
    "Admin",
    "Notification",
    "NotificationType",
    "NotificationChannel",
]

from models import User, RoleEnum

# Access the User model
user = User(email="patient@example.com", phone="9876543210", role=RoleEnum.PATIENT)
