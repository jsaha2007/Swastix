# Swastix - Project Progress
> Paste this entire file to GitHub Copilot and say "Resume from PROGRESS.md"

---

## Project
- **Name**: Swastix Doctor Booking System
- **Purpose**: Doctor booking system for rural India
- **GitHub**: https://github.com/jsaha2007/Swastix
- **IDE**: Visual Studio 2022, Terminal = Command Prompt
- **Python**: 3.14.0
- **venv**: `.venv\Scripts\activate.bat`
- **Run app**: `python main.py`
- **API docs**: http://127.0.0.1:8000/redoc

---

## Developer Profile
- Knows C# well, learning Python
- Always explain Python concepts with C# comparisons
- Developer writes the code, Copilot only guides
- Give hints and structure, not full code

---

## Tech Stack
- Framework: FastAPI
- ORM: SQLAlchemy 2.0
- Database: PostgreSQL
- Server: Uvicorn
- Validation: Pydantic
- Config: python-dotenv

---

## Roles
- Patient, Doctor, Admin

---

## Project Structure
```
SwastixPythonAPI/
??? .venv
??? models/
?   ??? base.py               BaseModel + AuditModel
?   ??? __init__.py           User model
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
??? repositories/
?   ??? __init__.py
?   ??? base_repository.py    COMPLETE
?   ??? patient_repository.py COMPLETE
?   ??? doctor_repository.py  COMPLETE
?   ??? appointment_repository.py  IN PROGRESS
??? .env
??? config.py
??? database.py
??? init_db.py
??? main.py
??? requirements.txt
```

---

## Phase Status
- Phase 1 - Database Layer: COMPLETE
- Phase 2 - Repository Layer: IN PROGRESS
- Phase 3 - Business Logic: PLANNED
- Phase 4 - API Layer: PLANNED

---

## Current Status
- **Stopped at**: Setting up Agent System (LangChain + Groq)
- **Next task**: Fix `test_groq.py` error to verify Groq connection works

## Agent System Plan
- Framework: LangChain + langchain-groq (both installed ?)
- AI Model: Groq (free) - API key added to .env ?
- Agents planned:
  - Agent PO: creates story from backlog
  - Agent Dev: reads story, writes code
  - Agent DataPreparer: creates test data
  - Agent QA: tests implementation
- Orchestrators: Doctor, Patient, Admin (3 central orchestrators)
- Triggered: automatically from backlog

## Pending - Fix Groq Test Error
- File: `test_groq.py` (in project root)
- Error: unknown (paste error next session)
- Code:
```python
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama3-8b-8192"
)

response = llm.invoke("Say hello in one sentence!")
print(response.content)
```

## Also Pending - Complete AppointmentRepository
- Add 3 more methods:
  - `get_by_doctor_and_status(doctor_id, status)`
  - `get_by_patient_and_status(patient_id, status)`
  - `get_doctor_appointments_by_date(doctor_id, date)`
- Then: `TimeslotRepository`, `UserRepository`

---

## Actual Code Written

### models/base.py
```python
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func
from database import Base

class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
```

### repositories/base_repository.py
```python
from sqlalchemy.orm import Session
from models.base import BaseModel
from typing import TypeVar, Generic, Type

T = TypeVar("T", bound=BaseModel)

class BaseRepository(Generic[T]):
    def __init__(self, db: Session, model: Type[T]):
        self.db = db
        self.model = model

    def get_by_id(self, id: int) -> T:
        return self.db.query(self.model).filter(self.model.id == id).first()

    def get_all(self) -> list[T]:
        return self.db.query(self.model).all()

    def create(self, obj: T) -> T:
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def delete(self, id: int) -> None:
        obj = self.get_by_id(id)
        if obj:
            self.db.delete(obj)
            self.db.commit()
```

### repositories/patient_repository.py
```python
from sqlalchemy.orm import Session
from repositories.base_repository import BaseRepository
from models.patient import Patient
from models import User

class PatientRepository(BaseRepository[Patient]):
    def __init__(self, db: Session):
        super().__init__(db, Patient)

    def get_by_userid(self, user_id: int) -> Patient:
        return self.db.query(self.model).filter(self.model.user_id == user_id).first()

    def get_by_city(self, city: str) -> list[Patient]:
        return self.db.query(self.model).filter(self.model.city == city).all()

    def get_by_email(self, email: str) -> Patient:
        return self.db.query(self.model)\
            .join(User, self.model.user_id == User.id)\
            .filter(User.email == email)\
            .first()

    def get_by_phone(self, phone: str) -> Patient:
        return self.db.query(self.model)\
            .join(User, self.model.user_id == User.id)\
            .filter(User.phone == phone)\
            .first()
```

### repositories/doctor_repository.py
```python
from sqlalchemy.orm import Session
from repositories.base_repository import BaseRepository
from models.doctor import Doctor, DoctorSpecialty
from models import User

class DoctorRepository(BaseRepository[Doctor]):
    def __init__(self, db: Session):
        super().__init__(db, Doctor)

    def get_by_userid(self, user_id: int) -> Doctor:
        return self.db.query(self.model).filter(self.model.user_id == user_id).first()

    def get_by_city(self, city: str) -> list[Doctor]:
        return self.db.query(self.model).filter(self.model.city == city).all()

    def get_by_specialization(self, specialization: DoctorSpecialty) -> list[Doctor]:
        return self.db.query(self.model).filter(self.model.specialization == specialization).all()

    def get_approved_doctors(self) -> list[Doctor]:
        return self.db.query(self.model).filter(self.model.is_approved == True).all()

    def get_doctors_by_fee_equal(self, fee: float) -> list[Doctor]:
        return self.db.query(self.model).filter(self.model.consultation_fee == fee).all()

    def get_doctors_by_fee_greater_than(self, fee: float) -> list[Doctor]:
        return self.db.query(self.model).filter(self.model.consultation_fee > fee).all()

    def get_doctors_by_fee_less_than(self, fee: float) -> list[Doctor]:
        return self.db.query(self.model).filter(self.model.consultation_fee < fee).all()

    def get_by_name(self, name: str) -> list[Doctor]:
        starts_with = self.db.query(self.model)\
            .filter(self.model.first_name.ilike(f"{name}%"))\
            .all()
        contains = self.db.query(self.model)\
            .filter(self.model.first_name.ilike(f"%{name}%"))\
            .filter(~self.model.first_name.ilike(f"{name}%"))\
            .all()
        return starts_with + contains
```

### repositories/appointment_repository.py (IN PROGRESS)
```python
from sqlalchemy.orm import Session
from datetime import datetime
from repositories.base_repository import BaseRepository
from models.appointment import Appointment, AppointmentStatus

class AppointmentRepository(BaseRepository[Appointment]):
    def __init__(self, db: Session):
        super().__init__(db, Appointment)

    def get_by_doctor(self, doctor_id: int) -> list[Appointment]:
        return self.db.query(self.model).filter(self.model.doctor_id == doctor_id).all()

    def get_by_patient(self, patient_id: int) -> list[Appointment]:
        return self.db.query(self.model).filter(self.model.patient_id == patient_id).all()

    def get_by_status(self, status: AppointmentStatus) -> list[Appointment]:
        return self.db.query(self.model).filter(self.model.status == status).all()

    def get_by_date(self, date: datetime) -> list[Appointment]:
        return self.db.query(self.model).filter(self.model.appointment_date == date).all()

    # TODO: Add these 3 methods next session:
    # get_by_doctor_and_status(self, doctor_id: int, status: AppointmentStatus)
    # get_by_patient_and_status(self, patient_id: int, status: AppointmentStatus)
    # get_doctor_appointments_by_date(self, doctor_id: int, date: datetime)
```

---

## Python Concepts Learned So Far
- `self` = `this` in C#
- `__init__` = Constructor in C#
- Indentation instead of `{}`
- `from x import y` = `using` in C#
- `@app.get("/")` decorator = `[HttpGet("/")]` in C#
- `async def` = `async Task` in C#
- `Generic[T]` + `TypeVar` = `<T>` generics in C#
- `super().__init__()` = `base()` in C#
- `ilike()` = case-insensitive SQL LIKE
- `~` = NOT in SQLAlchemy filters
- `list1 + list2` = `list1.Concat(list2).ToList()` in C#
