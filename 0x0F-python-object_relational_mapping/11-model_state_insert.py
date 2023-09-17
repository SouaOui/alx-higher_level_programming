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
    sentence = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(sentence.format(
        username, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # state = session.query(State.id).where(State.name == name_state).first()
    new_state = State(name='Louisiana')
    session.add(new_state)
    # Commit the session to persist the changes
    session.commit()
    # print(state) -> None so the add didn't return anything
    # state = session.query(State.id).where(State.name == 'Louisiana').first()
    state = session.query(State.id).where(State.name == new_state.name).first()
    print(state.id)
