from models import Vaikas, Tevas
from session import session


# vaikas = session.query(Vaikas).get(1)
# tevas1 = vaikas.tevai[0]
# vaikas.tevai.remove(tevas1)
# session.commit()

tevas = session.query(Tevas).get(2)
vaikas1 = tevas.vaikai[0]
tevas.vaikai.remove(vaikas1)
session.commit()
