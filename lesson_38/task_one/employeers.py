import datetime
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///employeers.db")
base = declarative_base()


class Employeers(base):
    __tablename__ = "Employeers"
    id = Column(Integer, primary_key=True)
    name = Column("Name", String)
    surname = Column("Surname", String)
    birth_date = Column("Date of birth", DateTime)
    position = Column("Position", String)
    salary = Column("Salary", Integer)
    work_since_date = Column(
        "Working since", DateTime, default=datetime.datetime.utcnow
    )

    def __init__(
        self,
        name: str,
        surname: str,
        birth_date: datetime,
        position: str,
        salary: int,
    ):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.position = position
        self.salary = salary

    def __repr__(self):
        return f"{self.id} {self.name} {self.surname} - {self.birth_date} - {self.position} - {self.work_since_date}"


base.metadata.create_all(engine)
