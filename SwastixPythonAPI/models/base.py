from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func
from database import Base

class BaseModel(Base):
    __abstract__ = True  # This class will not be created as a table in the database

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

