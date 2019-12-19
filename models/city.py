#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.place import Place


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    'DBStorage - Place'
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", backref="cities")
