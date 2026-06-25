"""
Database initialization script
Run this once to create all tables in the database
"""

from database import Base, engine
from models import (
    User, RoleEnum,
    OTP,
    Patient,
    Doctor, DoctorSpecialty,
    Timeslot, DayOfWeek, TimeslotStatus,
    Appointment, ConsultationType, AppointmentStatus,
    MedicalDocument, DocumentType,
    Rating,
    Prescription,
    Admin,
    Notification, NotificationType, NotificationChannel
)


def init_db():
    """Create all database tables"""
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("? All tables created successfully!")


def drop_db():
    """Drop all database tables (use with caution!)"""
    print("WARNING: This will delete all tables and data!")
    confirm = input("Type 'yes' to confirm: ")
    if confirm.lower() == "yes":
        Base.metadata.drop_all(bind=engine)
        print("? All tables dropped!")
    else:
        print("Cancelled.")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "drop":
        drop_db()
    else:
        init_db()
