import sqlite3

conn = sqlite3.connect("lectures.db")
c = conn.cursor()

with conn:
    c.execute(
        """CREATE TABLE IF NOT EXISTS
    lectures (
    pavadinimas text,
    destytojas text,
    trukme integer
    )"""
    )

with conn:
    c.execute("INSERT INTO lectures VALUES ('Vadyba', 'Domantas', 40)")
    c.execute("INSERT INTO lectures VALUES ('Python', 'Donatas', 80)")
    c.execute("INSERT INTO lectures VALUES ('Java', 'Tomas', 80)")

with conn:
    c.execute("SELECT * From lectures WHERE trukme>50")


with conn:
    c.execute(
        "UPDATE lectures SET pavadinimas='Python programavimas' WHERE pavadinimas='Python'"
    )

with conn:
    c.execute("DELETE from lectures WHERE destytojas='Tomas'")

with conn:
    c.execute("SELECT * From lectures")
    print(c.fetchall())
