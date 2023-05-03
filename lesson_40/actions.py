from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.orm import sessionmaker
from models.user import User
from models.task import Task


class SqliteDatabase:
    def __init__(self, filename: str, base: DeclarativeMeta) -> None:
        self.filename = filename
        self.base = base
        self.engine = create_engine(f"sqlite:///{self.filename}")
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def create_database(self) -> None:
        self.base.metadata.create_all(self.engine, checkfirst=True)

    def create_user(self, username: str, email: str, password: str) -> None: # user / task
        user = User(username=username, email=email, password=password)
        self.session.add(user)
        self.session.commit()

    def create_task(self, user: User, task_date_time: datetime, task_description: str) -> None: # user / task
        task = Task(end_date_time=task_date_time, description=task_description)
        user.tasks.append(task)
        self.session.add(user)
        self.session.commit()

    def update_object(self, object: DeclarativeMeta) -> None:
        self.session.merge(object)
        self.session.commit()

    def delete_object(self, object: DeclarativeMeta) -> None:
        self.session.delete(object)
        self.session.commit()

    def get_user(self, name: str) -> User:
        return self.session.query(User).filter_by(username=name).one()
    
    def get_task(self, id) -> Task:
        return self.session.query(Task).filter_by(id=id).one()
    
    def get_objects_by_username(self, username: str) -> None: # return
        object_list = self.session.query(Task).join(User).filter(User.username == username).all()
        for task in object_list:
            print(f'{task.id}. Description: {task.description}, Task end time: {datetime.strftime(task.end_date_time, "%Y-%m-%d %H:%M")}')

    def get_table_columns(self) -> None:
        print(f"There are table coluns:")
        headers = Task.__table__.columns.keys()
        for header in headers:
            print(f"{headers.index(header)+1} {header}")

    def chek_user(self, name:str, password:str) -> bool:
        try:
            user = self.session.query(User).filter_by(username=name).one()
        except:
            return False
        if user.password == password: 
            return True 
        return False


