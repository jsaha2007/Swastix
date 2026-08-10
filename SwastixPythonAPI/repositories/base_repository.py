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




