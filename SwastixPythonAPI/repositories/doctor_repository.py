from sqlalchemy.orm import Session
from repositories.base_repository import BaseRepository
from models.doctor import Doctor, DoctorSpecialty
from models import User

class DoctorRepository(BaseRepository[Doctor]):
    def __init__(self, db: Session):
        super().__init__(db, Doctor)

    def get_by_userid(self, user_id: int) -> Doctor:
       return self.db.query(self.model).filter(self.model.user_id == user_id).first()

    def get_by_name(self, name: str) -> list[Doctor]:
       starts_with = self.db.query(self.model)\
           .filter(self.model.first_name.ilike(f"{name}%"))\
           .all()
       contains = self.db.query(self.model)\
           .filter(self.model.first_name.ilike(f"%{name}%"))\
           .filter(~self.model.first_name.ilike(f"{name}%"))\
           .all()
       return starts_with + contains

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