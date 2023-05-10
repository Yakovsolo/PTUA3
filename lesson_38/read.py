from main import Project
from session import session

# projektai = session.query(Project).all()

# print(projektai)

project = session.query(Project).filter_by(name="2 projektas")

print(project)
