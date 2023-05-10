from datetime import datetime, date, time
from typing import Optional
from models import User, Task
from getpass import getpass
from session import session


def create_user() -> None:
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = getpass("Enter password: ")
    user = User(username=username, email=email, password=password)
    session.add(user)
    session.commit()
    print(f"User {username} created with id {user.id}")


def delete_user(username) -> None:
    user = session.query(User).filter_by(username=username).first()
    if user:
        session.delete(user)
        session.commit()
        print(f"User {user.username} with user ID {user.id} deleted")
    else:
        print(f"User {user.username} not found in base")


def log_in() -> Optional[User]:
    while True:
        username = input("Enter username: ")
        password = getpass("Enter password: ")
        user = (
            session.query(User).filter_by(username=username, password=password).first()
        )
        if user:
            print(f"Welcome back {user.username}!")
            return user
        else:
            print("Invalid username or password. Please try again.")
            log_in()


def logout():
    pass


def create_task(user) -> None:
    description = input("Enter task description: ")
    task_date = datetime.strptime(
        input("Input task's date (YYYY.MM.DD):\n"), "%Y.%m.%d"
    ).date()
    task_time = datetime.strptime(input("Input task's time (HH:MM):\n"), "%H:%M").time()
    task = Task(
        task_date=task_date,
        task_time=task_time,
        description=description,
        user_id=user.id,
    )
    session.add(task)
    session.commit()
    print(f"Task {task.id} created for user {user.username}")

def get_table_columns():
    print(f"There are table coluns:")
    headers = Task.__table__.columns.keys()
    for header in headers:
        print(f"{headers.index(header)+1} {header}")


# def get_user_tasks(user):




# def update_task(user, task_id):

#     task = session.query(Task).filter_by(user_id=user.id).first()
#     choice = int(input("Select which column you want to change\n "))
#     new_data = input("Enter new task description: ")
#     task.

    # if choice == 1:


    # for columns in task.items():
    #     new_description = 
    #     task.description = new_description
    #     session.commit()
    #     print(f"Task {task.id} updated for user {user.username}")
    # else:
    #     print(f"Task {task_id} not found for user {user.username}")


# helper function to delete a task for a user
# def delete_task(user):
#     task_id = input("Enter task id: ")
#     task = session.query(Task).filter_by(id=task_id, user_id=user.id).first()
#     if task:
#         session.delete(task)
#         session.commit()
#         print(f"Task {task.id} deleted for user {user.username}")
#     else:
#         print(f"Task {task_id} not found for user {user.username}")