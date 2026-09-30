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

## Groq Model Note (IMPORTANT)
- `llama-3.3-70b-versatile` was deprecated/unavailable — replaced with `openai/gpt-oss-120b` in `base_agent.py`
- Available chat models on this Groq account: `openai/gpt-oss-120b`, `openai/gpt-oss-20b`, `qwen/qwen3.6-27b`, `allam-2-7b`
- Other models in the account (whisper, orpheus, prompt-guard, compound) are NOT chat models — don't use for `execute()`

## File Encoding Note (IMPORTANT)
- Always use `encoding="utf-8"` when opening files for read/write in Python (LLM output can contain emojis/unicode that break default Windows `cp1252` encoding)
```python
with open(path, "w", encoding="utf-8") as f:
    ...
with open(path, "r", encoding="utf-8") as f:
    ...
```

## Debugging Note (IMPORTANT)
- VS Python debugger (F5) is broken with Python 3.14 (debugpy/pydevd incompatibility - AttributeError on threading internals)
- Workaround: use Ctrl+F5 (Run without debugging) + print() statements for now
- Can also run directly from plain cmd: `cd` into inner SwastixPythonAPI folder, `.venv\Scripts\activate.bat`, then `python file.py`

## Agent Call Chain - CONFIRMED DESIGN (Important Clarification)
- Developer/tests should NOT call PoAgent/DevAgent/etc directly in real usage — that's only for sanity tests
- Real flow: DoctorOrchestrator/PatientOrchestrator/AdminOrchestrator injects domain_context (Swastix + tech stack details) into the task BEFORE calling PoAgent.execute()
- This is WHY early sanity test output was generic/wrong tech stack — expected, since orchestrator (which injects context) doesn't exist yet
- Chain: Orchestrator.run(backlog_item) -> builds full_task = domain_context + backlog_item -> po.execute(full_task) -> story_path -> dev.execute(story_path) -> ... -> qa.execute(...)

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

## Teaching Style (IMPORTANT - Follow This Every Session)
- **Developer writes ALL code** — Copilot only gives hints and structure
- **Never write full solutions** unless explicitly asked
- Always explain Python concepts with C# comparisons
- Review code after developer writes it, point out issues with explanations
- Ask developer to paste their code for review before moving to next step
- Guide one file at a time, in order

## venv Correct Path
- `.venv` is inside the inner `SwastixPythonAPI` folder
- Full path: `C:\Drive D\Code\Own\Swastix\Swastrix_API\SwastixPythonAPI\SwastixPythonAPI\.venv\Scripts\python.exe`
- Always activate from: `C:\Drive D\Code\Own\Swastix\Swastrix_API\SwastixPythonAPI\SwastixPythonAPI`

## Current Status
- **Stopped at**: ALL THREE domain orchestrators COMPLETE - `doctor_orchestrator.py`, `patient_orchestrator.py`, `admin_orchestrator.py` all written, reviewed, and confirmed correct (imports verified against `base_orchestrator.py`)
- **Sanity test created**: `test_admin_orchestrator.py` (in project root, same folder as `test_po_agent.py`) - instantiates `AdminOrchestrator`, calls `.run("View reporting dashboard with daily booking and cancellation volume")`, prints all 5 result paths (story/code/review/data/tests). NOT YET RUN - developer will run it in a future session.
- **Next task**: Run `test_admin_orchestrator.py` to validate the full end-to-end pipeline (Po -> Dev -> CodeReviewer -> DataPreparer -> Qa) works for a real domain-contextualized backlog item. Then optionally write similar sanity tests for `doctor_orchestrator.py` / `patient_orchestrator.py`, or move to updating `PROGRESS.md` phase status and planning the next phase (full automation loop - see FUTURE PHASE VISION section).

## CONFIRMED PIPELINE ORDER (IMPORTANT - REVISED)
```
PoAgent (story) -> DevAgent (code) -> CodeReviewerAgent (review feedback) -> DataPreparerAgent (test data) -> QaAgent (test cases using code + data)
```
- CodeReviewerAgent added as a NEW agent (developer's own idea) - checks code quality/correctness/SOLID/repository pattern BEFORE tests are written
- Rationale: catch code issues early, don't waste effort writing tests for bad code
- DataPreparerAgent takes the STORY file (not code file) as input - test data should reflect business requirements, not implementation details (developer + copilot agreed)
- **REORDER REASON**: Originally QaAgent and DataPreparerAgent ran independently (QaAgent only saw code, DataPreparerAgent only saw story) - this meant QaAgent would invent placeholder data instead of using DataPreparerAgent's actual output. Fixed by moving DataPreparerAgent BEFORE QaAgent, and QaAgent.execute() now takes BOTH code_file_path and data_file_path as input, combining both into one prompt for the LLM.

## Agent Folder Structure
```
agents/
+-- __init__.py
+-- base_agent.py              DONE (saveToFile is now a shared generic method here)
+-- po_agent.py                DONE (uses self.saveToFile)
+-- dev_agent.py                DONE (uses self.saveToFile)
+-- code_reviewer_agent.py      DONE (NEW - reviews code quality, saves to CodeReviews/ folder)
+-- qa_agent.py                DONE (generates pytest test files, saves to Tests/ folder)
+-- data_preparer_agent.py      DONE (RENAMED from data_preparer.py -> data_preparer_agent.py, generates test data from story, saves to Data/ folder)
    +-- orchestrators/
    +-- __init__.py
    +-- base_orchestrator.py    DONE (chains all 5 agents in confirmed order, returns dict of file paths)
    +-- doctor_orchestrator.py  DONE
    +-- patient_orchestrator.py DONE
    +-- admin_orchestrator.py   DONE
```

## doctor_orchestrator.py / patient_orchestrator.py / admin_orchestrator.py - ALL COMPLETE ?
All three follow the same confirmed pattern - import `BaseOrchestrator`, no extra params in `__init__`, just supply a domain-specific `domain_context` string via `super().__init__(domain_context=...)`. No other methods needed.

```python
# admin_orchestrator.py (verified correct, imports confirmed against base_orchestrator.py)
from agents.orchestrators.base_orchestrator import BaseOrchestrator

class AdminOrchestrator(BaseOrchestrator):
    def __init__(self):
        super().__init__(
            domain_context="""Swastix Doctor Booking System.
            Admin can manage doctor and their schedule, manage patients and their appointments.
            Moreover, admin can get a reporting dashboard to view which contains daily volume,
            booking volume, cancellation volume, successfull visit volume"""
        )
```
- `doctor_orchestrator.py` and `patient_orchestrator.py` follow the identical shape with role-appropriate `domain_context` text (doctor: manages availability/schedule/prescriptions; patient: searches doctors, books appointments, views prescriptions).
- All imports verified consistent with `data_preparer_agent.py` rename and final pipeline order.
## FILE RENAME NOTE (IMPORTANT)
- `data_preparer.py` was RENAMED to `data_preparer_agent.py` for naming consistency with other agent files (po_agent.py, dev_agent.py, qa_agent.py, code_reviewer_agent.py)
- Any future import of DataPreparerAgent must use: `from agents.data_preparer_agent import DataPreparerAgent`

## base_orchestrator.py - COMPLETE
```python
from agents.po_agent import PoAgent
from agents.dev_agent import DevAgent
from agents.code_reviewer_agent import CodeReviewerAgent
from agents.data_preparer_agent import DataPreparerAgent
from agents.qa_agent import QaAgent

class BaseOrchestrator:
    def __init__(self, domain_context: str):
        self.domain_context = domain_context
        self.po = PoAgent()
        self.dev = DevAgent()
        self.code_reviewer = CodeReviewerAgent()
        self.data_preparer = DataPreparerAgent()
        self.qa = QaAgent()

    def run(self, backlog_item: str) -> dict:
        full_task = f"{self.domain_context}\n\nBacklog Item: {backlog_item}"
        story_path = self.po.execute(full_task)
        code_path = self.dev.execute(story_path)
        review_path = self.code_reviewer.execute(code_path)
        data_path = self.data_preparer.execute(story_path)
        test_path = self.qa.execute(code_path, data_path)

        return {
            "story": story_path,
            "code": code_path,
            "review": review_path,
            "data": data_path,
            "tests": test_path
        }
```

## doctor_orchestrator.py / patient_orchestrator.py / admin_orchestrator.py - What to Write Next
- Each inherits `BaseOrchestrator`
- Each `__init__` takes NO extra params, calls `super().__init__(domain_context="...")` with a domain-specific description (mention Swastix, FastAPI/SQLAlchemy/PostgreSQL tech stack, and the specific role's responsibilities - e.g. doctor manages availability/prescriptions, patient books appointments/searches doctors, admin approves doctors/manages platform)
- No other methods needed - all logic lives in BaseOrchestrator.run()
- Example shape:
```python
from agents.orchestrators.base_orchestrator import BaseOrchestrator

class DoctorOrchestrator(BaseOrchestrator):
    def __init__(self):
        super().__init__(
            domain_context="""..."""
        )
```


## base_agent.py - COMPLETE (refactored - now has shared saveToFile method)
```python
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from datetime import datetime
import uuid
import os

class BaseAgent:
    def __init__(self, role: str, goal: str):
        load_dotenv()
        self.role = role
        self.goal = goal
        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="openai/gpt-oss-120b"
        )

    def execute(self, task: str) -> str:
        prompt = f"You are a {self.role}. Your goal is {self.goal}. Task: {task}"
        response = self.llm.invoke(prompt)
        return response.content

    def saveToFile(self, text, parent_folder, file_name_prefix) -> str:
        os.makedirs(parent_folder, exist_ok=True)
        story_id = uuid.uuid4()
        id_str = str(story_id)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{file_name_prefix}_{id_str}_{timestamp}.txt"
        path = os.path.join(parent_folder, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"ID: {id_str}. Timestamp: {timestamp}\n")
            f.write(f"{text}\n")
        return path
```

## FUTURE PHASE VISION (Confirmed with Developer - Not Yet Implemented)
- Level 1 (current/today): Each agent generates text -> saves to file -> human manually reviews/copies into real project
- Future phase goal: FULL AUTOMATION LOOP:
  - CodeReviewerAgent's findings should automatically feed back into DevAgent to FIX the code (not just report issues)
  - QaAgent's generated tests should be automatically EXECUTED (e.g., via pytest subprocess)
  - If tests fail, feed failure output back to DevAgent to fix, then re-review, re-test (iterative loop until passing or max retries)
  - This matches the "Level 3 - Fully Automated" vision discussed earlier in the project (self-correcting agent loop)
- NOT started yet - current focus is Level 1 (orchestrator chaining agents, saving all outputs to files, human-in-the-loop)

## po_agent.py - COMPLETE (refactored - uses shared saveToFile)
```python
from agents.base_agent import BaseAgent

class PoAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Product Owner",
            goal="Define and prioritize product features and requirements and create the user stories."
        )

    def execute(self, task) -> str:
        story = super().execute(task)
        path = self.saveToFile(story, "UserStories", "story")
        return path
```

## dev_agent.py - COMPLETE
```python
from agents.base_agent import BaseAgent

class DevAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Developer",
            goal="""You are a backend developer working with FastAPI, SQLAlchemy 2.0, and PostgreSQL.
Read the given user story and implement the corresponding code.
Maintain SOLID Principals how much we can. Follow repository pattern for database connection.
The code flow should be Repository -> Service -> Controller and vice-versa.
Only output the code - no explanations, no markdown formatting, no extra text."""
        )

    def execute(self, story_file_path):
        with open(story_file_path, "r", encoding="utf-8") as f:
            content = f.read()
        code = super().execute(content)
        path = self.saveToFile(code, "Code", "code")
        return path
```

## Sanity Test Status
- DONE: `test_po_agent.py` ran successfully after fixing: model name, utf-8 encoding
- Output was generic/wrong tech stack - EXPECTED, since PoAgent is called directly without domain context (see Agent Call Chain note above). Will be fixed once DoctorOrchestrator exists.
- DEFERRED: sanity test for DevAgent (chained PoAgent -> DevAgent) - developer chose to keep building agents first, will test full chain later

## qa_agent.py - COMPLETE (UPDATED - now takes code + data as TWO inputs)
```python
from agents.base_agent import BaseAgent

class QaAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="QA Engineer",
            goal="""You are a QA engineer. You will be given a code snippet and you need to write test cases for it.
            The test cases should be written in pytest framework.
            The test cases should cover all possible edge cases and scenarios.
            You will be given both the code AND sample test data.
            Use the provided sample data directly in your test cases wherever applicable.
            The test cases should be written in a separate file named test_<original_file_name>.py
            Only output the code - no explanations, no markdown formatting, no extra text."""
        )

    def execute(self, code_file_path, data_file_path) -> str:
        with open(code_file_path, "r", encoding="utf-8") as f:
            code_content = f.read()
        with open(data_file_path, "r", encoding="utf-8") as f:
            data_content = f.read()

        combined_input = f"Code:\n{code_content}\n\nTest Data:\n{data_content}"
        test_code = super().execute(combined_input)
        path = self.saveToFile(test_code, "Tests", "test_code")
        return path
```
- IMPORTANT: execute() signature changed from `execute(code_file_path)` to `execute(code_file_path, data_file_path)` - orchestrator must pass BOTH paths when calling QaAgent

## code_reviewer_agent.py - COMPLETE (NEW AGENT)
```python
from agents.base_agent import BaseAgent

class CodeReviewerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Code Reviewer",
            goal="""check code quality, correctness, adherence to SOLID/repository pattern,
            find bugs, suggest fixes.
            List all the findings in a list and say no issues found if clean"""
        )

    def execute(self, code_file_path):
        with open(code_file_path, "r", encoding="utf-8") as f:
            content = f.read()
        review = super().execute(content)
        path = self.saveToFile(review, "CodeReviews", "review_code")
        return path
```

## data_preparer.py - COMPLETE
```python
from agents.base_agent import BaseAgent

class DataPreparerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Data Preparer",
            goal="""You are a data preparer. You will be given a user story and you need to prepare the data for it.
            The data should be prepared in a way that it can be used for testing the code generated from the user story.
            The data should be prepared in a separate file named data_<original_file_name>.py
            Only output the code - no explanations, no markdown formatting, no extra text."""
        )

    def execute(self, story_file_path):
        with open(story_file_path, "r", encoding="utf-8") as f:
            content = f.read()
        data_code = super().execute(content)
        path = self.saveToFile(data_code, "Data", "data_code")
        return path
```
- Takes STORY file path as input (developer + copilot agreed: test data should reflect business requirements, not code implementation details)
- Minor style nitpick (not fixed, optional): missing blank line between __init__ and execute (PEP8 cosmetic, same nitpick applied to qa_agent.py and code_reviewer_agent.py too)

## ALL 6 AGENT FILES + ALL 3 DOMAIN ORCHESTRATORS NOW COMPLETE ?????????
| Agent/Orchestrator | File | Status |
|-------|------|--------|
| BaseAgent | base_agent.py | DONE |
| PoAgent | po_agent.py | DONE |
| DevAgent | dev_agent.py | DONE |
| CodeReviewerAgent | code_reviewer_agent.py | DONE (NEW - not in original plan, added mid-session) |
| QaAgent | qa_agent.py | DONE |
| DataPreparerAgent | data_preparer_agent.py | DONE (renamed from data_preparer.py) |
| BaseOrchestrator | orchestrators/base_orchestrator.py | DONE |
| DoctorOrchestrator | orchestrators/doctor_orchestrator.py | DONE |
| PatientOrchestrator | orchestrators/patient_orchestrator.py | DONE |
| AdminOrchestrator | orchestrators/admin_orchestrator.py | DONE |

## Design Refactor Note (IMPORTANT)
- `saveToFile(text, parent_folder, file_name_prefix)` was moved from PoAgent into BaseAgent as a shared/reusable method (good DRY improvement, developer's own idea)
- ALL agents (Po, Dev, CodeReviewer, Qa, DataPreparer) now call `self.saveToFile(...)` instead of duplicating file-writing logic
- Known gotcha: file reads occasionally appeared stale/cached vs what's actually on disk during earlier session - if content looks wrong, verify directly via terminal (Get-Content) before assuming code is broken

## NEXT SESSION - START HERE
1. **Immediate next task**: Run `test_admin_orchestrator.py` (in project root) to validate the full pipeline end-to-end:
   ```
   cd into inner SwastixPythonAPI folder, .venv\Scripts\activate.bat, then:
   python test_admin_orchestrator.py
   ```
   This will call `AdminOrchestrator().run("View reporting dashboard with daily booking and cancellation volume")` and print paths for story/code/review/data/tests. Verify each generated file looks correct and reflects the Swastix admin domain context (not generic output).
2. If the admin sanity test passes, optionally write similar sanity tests for `doctor_orchestrator.py` and `patient_orchestrator.py` (same pattern - instantiate orchestrator, call `.run(backlog_item)`, print paths).
3. If any bugs surface during the run (e.g., import errors, encoding issues, bad LLM output), fix them in the relevant agent/orchestrator file - all agents and orchestrators are otherwise considered feature-complete.
4. After sanity testing is done, next big decision point: move toward FUTURE PHASE VISION (full automation loop - CodeReviewer findings feed back into DevAgent, QaAgent tests get executed via pytest subprocess, failures loop back to DevAgent) OR continue with Phase 4 (API layer) using the now-working agent system to actually generate real application code (repository/service/controller layers) as originally intended.
5. Cleanup reminder: qa_agent.py, code_reviewer_agent.py, data_preparer_agent.py all have a minor missing-blank-line PEP8 nitpick between __init__ and execute (cosmetic only, optional fix)

## Agent Architecture (Big Picture)
- **Agents** = Reusable, domain-agnostic AI workers powered by LangChain + Groq LLM
- **Orchestrators** = Swastix-specific, carry domain knowledge, coordinate agents
- **Flow**: Orchestrator receives a backlog item ? passes to PO ? Dev ? DataPreparer ? QA ? returns result
- **Goal**: Automate feature development pipeline using AI agents

## Overall Project Goal
Build a **Doctor Booking System for rural India** (FastAPI + PostgreSQL) with an **AI multi-agent system** on top that automates business logic using LLM agents.

## ?? IMPORTANT CLARIFIED INTENT (Read This First)
- **Developer hand-writes the entire Agent/Orchestrator system** (base_agent, po_agent, dev_agent, qa_agent, data_preparer, orchestrators) — this is the learning project.
- **Once the Agent system works, the AI agents (specifically DevAgent) will write the actual application code** — repository methods, API endpoints, business logic — NOT the developer.
- So remaining repository work (`appointment_repository.py` 3 methods, `TimeslotRepository`, `UserRepository`) and Phase 4 API endpoints should be LEFT UNFINISHED intentionally — they will later be generated by asking the working Agent system (via `DevAgent`/`PoAgent`) to implement them as a real test-run.
- **Current priority: 100% focus on finishing the Agent System (Phase 3) by hand.**



## Folder Structure to Create
```
agents/
??? __init__.py
??? base_agent.py              ? reusable base
??? po_agent.py                ? reusable
??? dev_agent.py               ? reusable
??? data_preparer.py           ? reusable
??? qa_agent.py                ? reusable
??? orchestrators/
    ??? __init__.py
    ??? base_orchestrator.py   ? reusable base
    ??? doctor_orchestrator.py ? Swastix specific
    ??? patient_orchestrator.py? Swastix specific
    ??? admin_orchestrator.py  ? Swastix specific
```

## Groq Setup - DONE ?
- langchain + langchain-groq installed
- GROQ_API_KEY in .env
- Model: llama-3.3-70b-versatile
- test_groq.py works successfully

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
