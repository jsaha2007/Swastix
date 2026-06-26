# Phase 1: Database Layer - Setup Guide

## Overview
This is Phase 1 of the Swastix Doctor Booking System. The database layer is now complete with all models, relationships, and configurations.

## Project Structure

```
SwastixPythonAPI/
??? config.py                    # Configuration settings
??? database.py                  # Database connection and session management
??? init_db.py                   # Database initialization script
??? .env                         # Environment variables (create from .env.example)
??? .env.example                 # Example environment variables
??? setup.bat                    # Setup script (Windows)
??? setup.sh                     # Setup script (Linux/Mac) - to be created
??? DATABASE_SCHEMA.md           # Database schema documentation
??? requirements.txt             # Python dependencies
??? models/
    ??? __init__.py              # Model exports
    ??? user.py                  # User model (base for all roles)
    ??? otp.py                   # OTP verification model
    ??? patient.py               # Patient profile model
    ??? doctor.py                # Doctor profile model
    ??? timeslot.py              # Doctor timeslots model
    ??? appointment.py           # Appointment/Booking model
    ??? prescription.py          # Prescription model
    ??? medical_document.py      # Medical documents (reports, etc.)
    ??? rating.py                # Doctor and visit ratings
    ??? admin.py                 # Admin profile model
    ??? notification.py          # Notification model
```

## Installation Steps

### 1. Update Environment Variables
Copy `.env.example` to `.env` and update with your PostgreSQL credentials:

```bash
cp .env.example .env
```

Edit `.env`:
```
DATABASE_URL=postgresql://your_username:your_password@localhost:5432/swastix_db
DEBUG=True
SECRET_KEY=your-secret-key-here
OTP_EXPIRY_MINUTES=10
OTP_LENGTH=6
```

### 2. Create PostgreSQL Database
```sql
-- Connect to PostgreSQL
createdb swastix_db

-- Or via psql:
psql -U postgres
CREATE DATABASE swastix_db;
```

### 3. Install Dependencies
```bash
# Activate virtual environment
python -m venv .venv
.venv\Scripts\activate.bat    # Windows
# or
source .venv/bin/activate     # Linux/Mac

# Install packages
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Initialize Database
This creates all tables in PostgreSQL:
```bash
python init_db.py
```

## Models Overview

### User (Base)
- `id`, `email`, `phone`, `role`, `is_active`, `is_verified`
- Roles: PATIENT, DOCTOR, ADMIN

### Patient
- Profile: first_name, last_name, DOB, gender, address
- Medical: medical_history, allergies, blood_group
- Preferences: consent_sms, consent_email

### Doctor
- Profile: name, specialization, qualification, license_number
- Professional: years_of_experience, bio
- Consultation: fee, duration
- Status: is_approved, is_active, average_rating

### Timeslot
- doctor_id, slot_date, start_time, end_time
- Status: AVAILABLE, BOOKED, BLOCKED
- Supports recurring slots and time-offs

### Appointment
- patient_id, doctor_id, timeslot_id
- Status: PENDING, CONFIRMED, COMPLETED, CANCELLED, NO_SHOW, RESCHEDULED
- Details: reason_for_visit, consultation_type (ONLINE/IN_PERSON)

### Prescription
- appointment_id, medicine_name, dosage, frequency, duration
- Instructions and notes

### MedicalDocument
- Stores: prescriptions, diagnosis reports, exam reports, lab reports
- Linked to patient and appointment

### Rating
- appointment_id, rate_doctor, rate_visit
- Includes review_text

### Notification
- Types: appointment confirmation, reminder, cancellation, OTP, etc.
- Channels: EMAIL, SMS, IN_APP

### Admin
- Permissions: manage_doctors, manage_patients, view_appointments, view_reports

## Key Features

? **OTP-based Authentication** - Email and phone verification
? **Role-based Access Control** - Patient, Doctor, Admin
? **Doctor Profiles** - Specialization, qualifications, ratings
? **Appointment Management** - Booking, rescheduling, cancellation
? **Timeslot Management** - Available slots, holidays, time-offs
? **Medical History** - Prescriptions, diagnosis reports, documents
? **Notification System** - SMS, Email, In-app notifications
? **Rating System** - Rate doctors and visits

## Enum Values

### DoctorSpecialty
- GENERAL, CARDIOLOGY, DERMATOLOGY, ORTHOPEDICS, PEDIATRICS, NEUROLOGY, PSYCHIATRY, ENT, OPHTHALMOLOGY, GYNECOLOGY, OTHER

### AppointmentStatus
- PENDING, CONFIRMED, COMPLETED, CANCELLED, NO_SHOW, RESCHEDULED

### ConsultationType
- ONLINE, IN_PERSON

### TimeslotStatus
- AVAILABLE, BOOKED, BLOCKED

## Database Relationships

```
User (1) ??? (1) Patient
         ??? (1) Doctor
         ??? (1) Admin
         ??? (*) Notification

Doctor (1) ??? (*) Timeslot
        ??? (*) Appointment
        ??? (*) Prescription
        ??? (*) Rating

Patient (1) ??? (*) Appointment
         ??? (*) MedicalDocument
         ??? (*) Prescription
         ??? (*) Rating

Appointment (1) ??? (*) MedicalDocument
            ??? (*) Prescription
            ??? (1) Rating
            ??? (*) Notification

Timeslot (1) ??? (*) Appointment
```

## Next Steps

### Phase 2: Repository Layer
- CRUD operations for all models
- Query builders and filters
- Data access patterns

### Phase 3: Business Logic Layer
- Service classes for business rules
- OTP generation and verification
- Appointment scheduling logic
- Notification triggers

### Phase 4: API Layer
- FastAPI endpoints for all operations
- Request/Response schemas (Pydantic)
- Error handling and validation
- Authentication middleware

## Troubleshooting

### Import Error: No module named 'sqlalchemy'
```bash
# Activate virtual environment and install dependencies
source .venv/bin/activate  # or .venv\Scripts\activate.bat
pip install -r requirements.txt
```

### Database Connection Error
Check `.env` file:
- Ensure DATABASE_URL is correct
- PostgreSQL server is running
- Database exists

### Table Creation Failed
```bash
# Drop all tables and recreate
python init_db.py drop  # Confirm with 'yes'
python init_db.py
```

## Quick Commands

```bash
# Activate virtual environment
.venv\Scripts\activate.bat

# Initialize database
python init_db.py

# Drop database (caution!)
python init_db.py drop

# Test imports
python -c "from models import User, Patient, Doctor; print('? Models OK')"
```

## Database Configuration

The database is configured with:
- **Driver**: psycopg2-binary (PostgreSQL)
- **ORM**: SQLAlchemy 2.0
- **Connection Pool**: 10 pool size, 20 max overflow
- **Timezone**: UTC (all timestamps stored with timezone)

---

**Status**: ? Phase 1 Complete - Database Layer Ready
**Next**: Phase 2 - Repository Layer Implementation
