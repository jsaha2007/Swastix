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