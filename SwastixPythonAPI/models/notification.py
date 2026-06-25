from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean, Enum
from sqlalchemy.sql import func
from database import Base
import enum


class NotificationType(str, enum.Enum):
    """Type of notification"""
    APPOINTMENT_CONFIRMATION = "appointment_confirmation"
    APPOINTMENT_REMINDER = "appointment_reminder"
    APPOINTMENT_CANCELLED = "appointment_cancelled"
    APPOINTMENT_RESCHEDULED = "appointment_rescheduled"
    OTP_VERIFICATION = "otp_verification"
    RATING_REQUEST = "rating_request"
    OTHER = "other"


class NotificationChannel(str, enum.Enum):
    """Notification delivery channel"""
    EMAIL = "email"
    SMS = "sms"
    IN_APP = "in_app"


class Notification(Base):
    """Notifications for users"""
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)

    # Notification Details
    notification_type = Column(Enum(NotificationType), nullable=False, index=True)
    channel = Column(Enum(NotificationChannel), nullable=False)

    # Content
    subject = Column(String(255), nullable=True)
    message = Column(Text, nullable=False)

    # Reference
    appointment_id = Column(Integer, ForeignKey("appointments.id"), nullable=True)

    # Status
    is_sent = Column(Boolean, default=False, index=True)
    is_read = Column(Boolean, default=False, index=True)
    sent_at = Column(DateTime(timezone=True), nullable=True)

    # Retry logic
    retry_count = Column(Integer, default=0)
    last_retry_at = Column(DateTime(timezone=True), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<Notification(id={self.id}, type={self.notification_type}, sent={self.is_sent})>"
