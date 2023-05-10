from main import Project
from session import session

project1 = session.query(Project).get(1)
project1.price = 22000
session.commit()
