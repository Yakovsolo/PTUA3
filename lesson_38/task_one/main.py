from employeers import Employeers
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import exit
from datetime import date, datetime


engine = create_engine("sqlite:///employeers.db")
Session = sessionmaker(bind=engine)
session = Session()
""":type: sqlalchemy.orm.Session"""

while True:
    selection = int(
        input(
            "Select an action : \n1 - print base of employeers \n2 - add new employee \n3 - update employee \n4 - delete employee\n5 - exit\n"
        )
    )
    print("-------------------")
    if selection == 1:
        employeers = session.query(Employeers).all()
        print("-------------------")
        for employee in employeers:
            print(employee)
        print("-------------------")

    if selection == 2:
        name = input("Input employee's name:\n")
        surname = input("Input employee's surname:\n")
        birth_date = datetime.strptime(
            (input("Input employee's date of birth (YYYY-MM-DD):\n")), "%Y-%M-%d"
        ).date()
        position = input("Input employee's position:\n")
        salary = int(input("Input employee's salary:\n"))
        employee = Employeers(name, surname, birth_date, position, salary)
        session.add(employee)
        session.commit()

    if selection == 3:
        employeers = session.query(Employeers).all()
        print("-------------------")
        for employee in employeers:
            print(employee)
        print("-------------------")
        changing_employee_id = int(
            input("Select the ID of the employee whose data you want to change:\n")
        )
        changing_employee = session.query(Employeers).get(changing_employee_id)
        change = int(
            input(
                "What do you like to change?:\n 1 - name\n 2 - surname\n 3 - date of birth\n 4 - position\n 5 - salary\n"
            )
        )
        if change == 1:
            changing_employee.name = input("Input employee's name:\n")
        if change == 2:
            changing_employee.surname = input("Input employee's surname:\n")
        if change == 3:
            changing_employee.birth_date = input(
                "Input employee's date of birth (YYYY-MM-DD):\n"
            )
        if change == 4:
            changing_employee.position = input("Input employee's position:\n")
        if change == 5:
            changing_employee.salary = int(input("Input employee's salary:\n"))
        session.commit()

    if selection == 4:
        employeers = session.query(Employeers).all()
        print("-------------------")
        for employee in employeers:
            print(employee)
        print("-------------------")
        delete_id = int(input("Select the ID of the employee you want to delete:\n"))
        delete_employee = session.query(Employeers).get(delete_id)
        session.delete(delete_employee)
        session.commit()

    if selection == 5:
        exit()
