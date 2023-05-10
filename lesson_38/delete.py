from main import Project
from session import session


projektas1 = session.query(Project).filter_by(name="Naujas pr.").one()

session.delete(projektas1)
session.commit()
