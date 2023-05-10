from models import Vaikas, Tevas
from session import session

vaikas = Vaikas(
    vardas="Sekejas 1",
    pavarde="Vaikaitis",
)
vaikas2 = Vaikas(
    vardas="Sekejas 2",
    pavarde="Vaikaitis 2",
)
tevas = Tevas(
    vardas="Jezus",
    pavarde="Vaikaitis",
)
tevas.vaikai.append(vaikas)
tevas.vaikai.append(vaikas2)
session.add(tevas)
session.commit()
