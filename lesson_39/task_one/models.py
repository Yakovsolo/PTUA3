from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine("sqlite:///users_to_do_base.db")
Base = declarative_base()


# create User model
class User(Base):  # type: ignore
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column("Username", String, unique=True, nullable=False)
    email = Column("Email", String, unique=True, nullable=False)
    password = Column("Password", String, nullable=False)
    tasks = relationship("Task", back_populates="user")


# create Task model
class Task(Base):  # type: ignore
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    user_id = Column("User ID", Integer, ForeignKey("users.id"))
    task_date = Column("Date", DateTime)
    task_time = Column("Time", DateTime)
    description = Column("Description", String, nullable=False)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
