#!/usr/bin/python3
"""Fetch All the Data From the table states"""
import sys
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name_state = sys.argv[4]
    sentence = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(sentence.format(
        username, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # state = session.query(State.id).where(State.name == name_state).first()
    state = session.query(State.id).filter(State.name.like(name_state)).first()
    if state:
        print(state.id)
    else:
        print('Not found')
