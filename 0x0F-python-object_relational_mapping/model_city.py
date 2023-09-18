#!/usr/bin/python3
"""Declaration of the Class City"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """Create a City class to represent the cities table in db

    Attributes:
        City  (id): id of the state
        City  (name): name of the state
        City  (state_id): id of the state which city belong to
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship('State', backref="cities")
