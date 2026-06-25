from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from database import Base
from datetime import datetime, timedelta
from config import OTP_EXPIRY_MINUTES


class OTP(Base):
    """OTP model for email and phone verification"""
    __tablename__ = "otps"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), index=True, nullable=True)
    phone = Column(String(20), index=True, nullable=True)
    otp_code = Column(String(10), nullable=False)
    is_used = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    expires_at = Column(DateTime(timezone=True), nullable=False)
    verified_at = Column(DateTime(timezone=True), nullable=True)

    def is_valid(self) -> bool:
        """Check if OTP is still valid and unused"""
        return not self.is_used and datetime.utcnow() < self.expires_at

    def __repr__(self):
        return f"<OTP(id={self.id}, contact={'email' if self.email else 'phone'}, is_valid={self.is_valid()})>"
