from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Enum, Float
from sqlalchemy.sql import func
from database import Base
import enum


class ConsultationType(str, enum.Enum):
    """Type of consultation"""
    ONLINE = "online"
    IN_PERSON = "in_person"


class AppointmentStatus(str, enum.Enum):
    """Appointment status"""
    PENDING = "pending"
    CONFIRMED = "confirmed"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    NO_SHOW = "no_show"
    RESCHEDULED = "rescheduled"


class Appointment(Base):
    """Appointment/Booking model"""
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False, index=True)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False, index=True)
    timeslot_id = Column(Integer, ForeignKey("timeslots.id"), nullable=True, index=True)

    # Appointment Details
    appointment_date = Column(DateTime(timezone=True), nullable=False, index=True)
    start_time = Column(DateTime(timezone=True), nullable=False)
    end_time = Column(DateTime(timezone=True), nullable=False)

    # Consultation Type
    consultation_type = Column(Enum(ConsultationType), default=ConsultationType.IN_PERSON)

    # Reason and Notes
    reason_for_visit = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)

    # Status
    status = Column(Enum(AppointmentStatus), default=AppointmentStatus.PENDING, index=True)

    # Cancellation Details
    cancellation_reason = Column(Text, nullable=True)
    cancelled_by = Column(String(50), nullable=True)  # patient, doctor, admin
    cancelled_at = Column(DateTime(timezone=True), nullable=True)

    # Confirmation
    is_confirmed = Column(String(50), default=False)  # Can track who confirmed

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<Appointment(id={self.id}, patient_id={self.patient_id}, doctor_id={self.doctor_id}, status={self.status})>"
