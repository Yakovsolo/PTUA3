from datetime import datetime, time
from sqlalchemy import create_engine
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.orm import sessionmaker
from models.user import User
from models.task import Task
from db.base import Base
from actions import SqliteDatabase
from functions import welcome, first_input_selection, second_input_selection
import getpass
import sys

tm = SqliteDatabase("Task_manager.db", Base)
tm.create_database()

welcome()
while True:
    selection = first_input_selection()
        
    if selection == 1:
        username = input("Please enter your username:\n")
        email = input("Please enter your email\n")
        password = getpass.getpass("Please enter your password:\n")
        user = User(username=username, email=email, password=password)
        tm.create_object(user)

    if selection == 2:
        username = input("Please enter your username:\n")
        password = getpass.getpass("Please enter your password:\n")
        if tm.chek_user(name=username, password=password):
            print("Access granted")
            user = tm.get_user(name=username)
            while True:
                second_selection = second_input_selection()
                if second_selection == 1:
                    task_date_time = datetime.strptime(input("Enter the end date of the task (YYYY-MM-DD HH:MM):\n"), "%Y-%m-%d %H:%M")
                    task_description = input("Enter the description of the task:\n")
                    task = Task(end_date_time=task_date_time, description=task_description)
                    user.tasks.append(task)
                    tm.create_object(task)
                
                if second_selection == 2:
                    tm.get_objects_by_username(username, user)
                    # task_date_time = datetime.strptime(input("Enter the end date of the task (YYYY-MM-DD HH:MM):\n"), "%Y-%m-%d %H:%M")
                    # task_description = input("Enter the description of the task:\n")
                    # task = Task(end_date_time=task_date_time, description=task_description)
                    # user.tasks.append(task)
                    # tm.create_object(task)


        else:
            print("Wrong username or password")

    if selection == 3:
        sys.exit("Task manager closed")

