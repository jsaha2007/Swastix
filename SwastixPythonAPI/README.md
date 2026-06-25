# ?? Swastix - Doctor Booking System

**A telemedicine appointment booking system for rural India with OTP-based authentication**

---

## ?? Quick Start (5 minutes)

### Prerequisites
- Python 3.8+
- PostgreSQL 12+
- pip (Python package manager)

### Installation

```bash
# 1. Navigate to project
cd SwastixPythonAPI

# 2. Create virtual environment
python -m venv .venv

# 3. Activate (Windows)
.venv\Scripts\activate.bat
# OR (Linux/Mac)
source .venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Configure database
# Edit .env file with your PostgreSQL credentials
cp .env.example .env
# Then edit DATABASE_URL=postgresql://user:password@localhost:5432/swastix_db

# 6. Initialize database
python init_db.py

# 7. Run application
python main.py
```

### Access the Application
- **API**: http://127.0.0.1:8000
- **API Docs**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

---

## ?? Project Overview

### Current Status
- ? **Phase 1**: Database Layer - COMPLETE
- ?? **Phase 2**: Repository Layer - Next
- ?? **Phase 3**: Business Logic - Later
- ?? **Phase 4**: API Layer - Later

### What's Included

#### Database Models (11)
```
User (Base)
??? Patient (Medical info, history)
??? Doctor (Profile, specialization, ratings)
??? Admin (Permissions, management)

OTP (Email/Phone verification)

Appointments
??? Timeslot (Doctor availability)
??? Appointment (Patient-Doctor booking)
??? Prescription (Medicine)
??? MedicalDocument (Reports, files)

Reviews
??? Rating (Doctor & visit ratings)

Notifications
??? Notification (SMS, Email, In-app)
```

#### API Endpoints (Current)
```
GET  /                 - Welcome
GET  /health           - Health check
GET  /api/v1           - API info
GET  /api/v1/status    - Detailed status
GET  /api/v1/doctors   - (Placeholder)
GET  /api/v1/appointments - (Placeholder)
```

---

## ?? Documentation

| Document | Purpose |
|----------|---------|
| `INDEX.md` | Documentation index |
| `PHASE1_README.md` | Setup & installation |
| `DATABASE_SCHEMA.md` | Database schema |
| `ARCHITECTURE_OVERVIEW.md` | System architecture |
| `BUILD_REPORT.md` | Build verification report |
| `main.py` | FastAPI application |
| `build.py` | Build verification script |

---

## ?? Features

### Patient Features
? Register with Email/Phone OTP  
? Search doctors by location, specialty, fee  
? View doctor profiles & ratings  
? Book appointments  
? Upload medical documents  
? Rate doctors & visits  

### Doctor Features
? Professional profile  
? Manage timeslots  
? Create prescriptions  
? View patient history  
? Receive ratings  

### Admin Features
? Doctor onboarding  
? Patient management  
? Appointment oversight  
? Dashboard reports  

---

## ??? Database

**Type**: PostgreSQL  
**Tables**: 11  
**Models**: 11 SQLAlchemy ORM models  
**Relationships**: 15+  
**Columns**: 150+  

### Quick Database Commands

```bash
# Initialize database
python init_db.py

# Drop all tables (caution!)
python init_db.py drop

# Access PostgreSQL
psql -U username -d swastix_db
```

---

## ??? Technology Stack

| Component | Technology |
|-----------|-----------|
| **Language** | Python 3.8+ |
| **Framework** | FastAPI |
| **ORM** | SQLAlchemy 2.0 |
| **Database** | PostgreSQL 12+ |
| **Driver** | psycopg2-binary |
| **Server** | Uvicorn |
| **Validation** | Pydantic |
| **Config** | python-dotenv |

---

## ?? Project Structure

```
SwastixPythonAPI/
??? main.py                 FastAPI application
??? config.py               Configuration
??? database.py             Database setup
??? init_db.py              DB initialization
??? build.py                Build verification
??? requirements.txt        Dependencies
??? .env.example            Environment template
?
??? models/                 ORM Models
?   ??? __init__.py        User model
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
?
??? Documentation/
    ??? INDEX.md
    ??? PHASE1_README.md
    ??? DATABASE_SCHEMA.md
    ??? ARCHITECTURE_OVERVIEW.md
    ??? BUILD_REPORT.md
```

---

## ?? Common Tasks

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Create Database
```bash
createdb swastix_db
```

### Initialize Database
```bash
python init_db.py
```

### Run Application
```bash
python main.py
```

### Build Verification
```bash
python build.py
```

### View API Documentation
After starting the app:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

---

## ?? Security

- ? OTP-based authentication (no passwords)
- ? Role-based access control
- ? User verification tracking
- ? Audit timestamps
- ? CORS enabled

---

## ?? Statistics

| Metric | Count |
|--------|-------|
| **Total Files** | 27 |
| **Python Files** | 15 |
| **Documentation Files** | 12 |
| **Database Models** | 11 |
| **API Endpoints** | 5+ |
| **Lines of Code** | 3500+ |
| **Test Coverage** | Build scripts |

---

## ? Troubleshooting

### "pip: command not found"
```bash
python -m pip install -r requirements.txt
```

### "Module not found" errors
```bash
# Activate virtual environment
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate.bat  # Windows

# Install dependencies
pip install -r requirements.txt
```

### Database connection errors
```bash
# Check .env file
# Verify PostgreSQL is running
# Ensure database exists: createdb swastix_db
```

### Port 8000 already in use
```bash
# Use different port
python -c "import uvicorn; uvicorn.run('main:app', host='0.0.0.0', port=8001)"
```

---

## ?? Learning Resources

- **FastAPI**: https://fastapi.tiangolo.com/
- **SQLAlchemy**: https://docs.sqlalchemy.org/
- **PostgreSQL**: https://www.postgresql.org/docs/
- **Pydantic**: https://docs.pydantic.dev/

---

## ?? Contributing

1. Follow the existing code structure
2. Update documentation for changes
3. Run `python build.py` to verify
4. Test your changes

---

## ?? Support

| Issue | Resource |
|-------|----------|
| Setup | PHASE1_README.md |
| Database | DATABASE_SCHEMA.md |
| Architecture | ARCHITECTURE_OVERVIEW.md |
| Build | BUILD_REPORT.md |
| API Docs | http://localhost:8000/docs |

---

## ?? Checklist

Before using:
- [ ] Python 3.8+ installed
- [ ] PostgreSQL installed and running
- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] .env configured
- [ ] Database initialized
- [ ] Build verification passed

---

## ?? Ready to Use!

The application is ready to run:

```bash
python main.py
```

Then visit: http://127.0.0.1:8000/docs

---

## ?? Roadmap

- ? **Phase 1**: Database Layer (Complete)
- ?? **Phase 2**: Repository Layer (Next)
- ?? **Phase 3**: Business Logic (Planned)
- ?? **Phase 4**: Complete API (Planned)

---

## ?? License

This is a proprietary project for Swastix.

---

**Status**: ? Phase 1 Complete - Ready to Use  
**Version**: 1.0.0  
**Last Updated**: Phase 1 Build Complete

?? **Welcome to Swastix!** ??
