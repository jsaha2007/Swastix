from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.sql import func
from database import Base


class Admin(Base):
    """Admin model"""
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False, index=True)

    # Personal Information
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)

    # Permissions (can be extended with more granular control)
    can_manage_doctors = Column(Boolean, default=True)
    can_manage_patients = Column(Boolean, default=True)
    can_view_appointments = Column(Boolean, default=True)
    can_view_reports = Column(Boolean, default=True)
    can_manage_admins = Column(Boolean, default=False)

    # Status
    is_active = Column(Boolean, default=True, index=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<Admin(id={self.id}, name={self.first_name} {self.last_name})>"
