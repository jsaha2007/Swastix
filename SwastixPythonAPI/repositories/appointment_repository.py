from sqlalchemy.orm import Session
from datetime import datetime
from repositories.base_repository import BaseRepository
from models.doctor import Doctor
from models.patient import Patient
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
       return self.db.query(self.model).filter(self.model.date == date).all()