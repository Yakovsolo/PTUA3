from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from db.base import Base


class Task(Base):  # type: ignore
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    user_id = Column("User ID", Integer, ForeignKey("users.id"))
    end_date_time = Column("Date", DateTime)
    description = Column("Description", String, nullable=False)
    users = relationship("User", back_populates="tasks")
