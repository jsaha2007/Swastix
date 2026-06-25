from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Float
from sqlalchemy.sql import func
from database import Base


class Rating(Base):
    """Ratings for doctors and visits"""
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)
    appointment_id = Column(Integer, ForeignKey("appointments.id"), nullable=False, unique=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False, index=True)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False, index=True)

    # Rating Details
    rating_score = Column(Float, nullable=False)  # 1-5 stars
    review_text = Column(Text, nullable=True)

    # What is being rated
    rate_doctor = Column(Float, nullable=False)  # Rating for the doctor
    rate_visit = Column(Float, nullable=False)   # Rating for the visit/appointment experience

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<Rating(id={self.id}, appointment_id={self.appointment_id}, score={self.rating_score})>"
