from sqlalchemy import String, Integer, Boolean
from sqlalchemy.orm import Mapped, MappedColumn
from .database import Base

class Task(Base):
    __tablename__ = "Tasks"

    id: Mapped[int] = MappedColumn(Integer, primary_key = True, index = True)
    title: Mapped[String] = MappedColumn(String, nullable=False)
    completed: Mapped[Boolean] =  MappedColumn(Boolean, nullable=False, default = False)