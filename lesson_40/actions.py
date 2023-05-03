from sqlalchemy import create_engine
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.orm import sessionmaker
from models.user import User


class SqliteDatabase:
    def __init__(self, filename: str, base: DeclarativeMeta):
        self.filename = filename
        self.base = base
        self.engine = create_engine(f"sqlite:///{self.filename}")
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def create_database(self):
        self.base.metadata.create_all(self.engine, checkfirst=True)

    def create_object(self, object: DeclarativeMeta):
        self.session.add(object)
        self.session.commit()

    def update_object(self, object: DeclarativeMeta):
        self.session.merge(object)
        self.session.commit()

    def delete_object(self, object: DeclarativeMeta):
        self.session.delete(object)
        self.session.commit()

    def get_user(self, name: str):
        return self.session.query(User).filter_by(username=name).one()
    
    def get_objects_by_username(self, username: str, object_type: DeclarativeMeta):
        object_list = self.session.query(object_type).filter(object_type.username == username).all()
        for object in object_list:
            print(object)
         

    def get_all_objects(self, object_type: DeclarativeMeta):
        return self.session.query(object_type).all().filter_by()
    
    def chek_user(self, name:str, password:str) -> bool:
        try:
            user = self.session.query(User).filter_by(username=name).one()
        except:
            return False
        if user.password == password: 
            return True 
        return False


