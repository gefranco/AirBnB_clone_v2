#!/usr/bin/python3
"""This is the state class"""
import models
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128))
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        @property
        def cities(self):
            all_objs_list = []
            all_objs = models.storage.all(City)

            for city in all_objs.values():
                if city.state_id == self.id:
                    all_objs_list.append(city)
            return all_objs_list
