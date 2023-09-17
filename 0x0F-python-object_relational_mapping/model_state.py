#!/usr/bin/python3
"""Declaration of the Class State"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

if __name__ == "__main__":
    class State(Base):
        """Create a State class to represent the states table in db

        Args:
            State  (id): id of the state
            state  (name): name of the state
        """
        __tablename__ = 'states'

        id = Column(Integer, primary_key=True)
        name = Column(String(128), nullable=False)
