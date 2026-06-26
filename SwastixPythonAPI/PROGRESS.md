# Swastix - Project Progress

## Project
- **Name**: Swastix Doctor Booking System
- **Purpose**: Doctor booking system for rural India
- **GitHub**: https://github.com/jsaha2007/Swastix
- **Language**: Python (developer is a C# developer, beginner in Python)

---

## Tech Stack
- **Framework**: FastAPI
- **ORM**: SQLAlchemy 2.0
- **Database**: PostgreSQL
- **Server**: Uvicorn
- **Validation**: Pydantic
- **Config**: python-dotenv
- **IDE**: Visual Studio 2022
- **Python**: 3.14.0

---

## Roles
- Patient
- Doctor
- Admin

---

## Project Structure
```
SwastixPythonAPI/
??? .venv                   Virtual environment
??? models/                 Database models (Phase 1)
?   ??? __init__.py         User model
?   ??? otp.py
?   ??? patient.py
?   ??? doctor.py
?   ??? timeslot.py
?   ??? appointment.py
?   ??? prescription.py
?   ??? medical_document.py
?   ??? rating.py
?   ??? admin.py
?   ??? notification.py
??? .env                    Database connection config
??? config.py               Reads .env settings
??? database.py             SQLAlchemy engine setup
??? init_db.py              Creates database tables
??? main.py                 FastAPI app + current endpoints
??? requirements.txt        Python dependencies
```

---

## Phases

### Phase 1 - Database Layer ? COMPLETE
- 11 SQLAlchemy models created
- Models: User, OTP, Patient, Doctor, Timeslot, Appointment, Prescription, MedicalDocument, Rating, Admin, Notification
- FastAPI app skeleton created in `main.py`
- Health check endpoints working
- App runs on http://127.0.0.1:8000
- API docs visible at http://127.0.0.1:8000/redoc

### Phase 2 - Repository Layer ?? NEXT
- Base repository class (parent class all others inherit from)
- UserRepository
- PatientRepository
- DoctorRepository
- AppointmentRepository
- TimeslotRepository
- Location: `repositories/` folder (to be created)

### Phase 3 - Business Logic Layer ? PLANNED
- Service classes
- Business rules
- OTP logic
- Notification triggers

### Phase 4 - API Layer ? PLANNED
- Full FastAPI endpoints
- Pydantic request/response schemas
- Authentication middleware

---

## Current Status
- **Stopped at**: About to start Phase 2 - Repository Layer
- **Next task**: Create `repositories/` folder and `base_repository.py`
- **Concept to explain**: Base Repository class (like a base class in C#)

---

## Learning Notes (Developer is learning Python via C#)
- Developer knows C# well
- Use C# comparisons when explaining Python concepts
- Key differences covered so far:
  - No type declarations needed in Python
  - `self` = `this` in C#
  - `__init__` = Constructor in C#
  - Indentation instead of `{}`
  - `@app.get("/")` decorator = `[HttpGet("/")]` in C#
  - `async def` = `async Task` in C#

---

## How to Resume
Paste this file content to GitHub Copilot chat and say:
**"Resume from PROGRESS.md"**
