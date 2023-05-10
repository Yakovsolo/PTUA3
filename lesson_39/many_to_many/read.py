from models import Tevas, Vaikas
from session import session


tevas = session.query(Tevas).get(2)
for vaikas in tevas.vaikai:
    print(vaikas.vardas, vaikas.pavarde)


print("-------------------")


tevas = session.query(Tevas).get(1)
for vaikas in tevas.vaikai:
    print(vaikas.vardas, vaikas.pavarde)

print("-------------------")

vaikas = session.query(Vaikas).get(1)
for tevas in vaikas.tevai:
    print(tevas.vardas, tevas.pavarde)
