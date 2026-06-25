from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Enum, Time
from sqlalchemy.sql import func
from database import Base
import enum
from datetime import time


class DayOfWeek(str, enum.Enum):
    """Days of the week"""
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"


class TimeslotStatus(str, enum.Enum):
    """Timeslot status"""
    AVAILABLE = "available"
    BOOKED = "booked"
    BLOCKED = "blocked"  # For holidays, time-offs, etc.


class Timeslot(Base):
    """Doctor timeslots for appointments"""
    __tablename__ = "timeslots"

    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False, index=True)

    # Date and Time
    slot_date = Column(DateTime(timezone=True), nullable=False, index=True)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)

    # Status
    status = Column(Enum(TimeslotStatus), default=TimeslotStatus.AVAILABLE, index=True)

    # For recurring slots (weekly pattern)
    day_of_week = Column(Enum(DayOfWeek), nullable=True)  # If recurring
    is_recurring = Column(Boolean, default=False)

    # Notes (for blocked slots)
    notes = Column(String(500), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<Timeslot(id={self.id}, doctor_id={self.doctor_id}, date={self.slot_date}, status={self.status})>"
