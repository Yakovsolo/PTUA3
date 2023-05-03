from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.base import Base


class User(Base):  # type: ignore
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column("Username", String, unique=True, nullable=False)
    email = Column("Email", String, unique=True, nullable=False)
    password = Column("Password", String, nullable=False)
    tasks = relationship("Task", back_populates="users")
