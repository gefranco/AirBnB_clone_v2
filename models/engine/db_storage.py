#!/usr/bin/python3
'''
'''
import os
from sqlalchemy import (create_engine)
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class DBStorage:
    '''
    '''
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(os.getenv("HBNB_MYSQL_USER"),
            os.getenv("HBNB_MYSQL_PWD"), 
            os.getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)
        





    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)
    
    def new(self, obj):

        if obj:
            self.__session.add(obj)
            
    

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)
            self.save()

    def all(self, cls=None):
        all_objs = {} 

        if cls:
            for obj in self.__session.query(cls):
                key = "{}.{}".format(type(obj).__name__, obj.id)
                all_objs[key] = obj
            return all_objs

        else:

            for obj in self.__session.query(User):
                key = "{}.{}".format(type(obj).__name__, obj.id)
                all_objs[key] = obj
            for obj in self.__session.query(State):
                key = "{}.{}".format(type(obj).__name__, obj.id)
                all_objs[key] = obj
            
            for obj in self.__session.query(City):
                key = "{}.{}".format(type(obj).__name__, obj.id)
                all_objs[key] = obj

            for obj in self.__session.query(Amenity):
                key = "{}.{}".format(type(obj).__name__, obj.id)
                all_objs[key] = obj

            for obj in self.__session.query(Place):
                key = "{}.{}".format(type(obj).__name__, obj.id)
                all_objs[key] = obj

            for obj in self.__session.query(Review):
                key = "{}.{}".format(type(obj).__name__, obj.id)
                all_objs[key] = obj

        return all_objs
            

    def close(self):
        self.__session.remove()
