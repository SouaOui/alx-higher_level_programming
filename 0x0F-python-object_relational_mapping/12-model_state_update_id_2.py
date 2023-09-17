#!/usr/bin/python3
"""
changes the name of a State object from the database hbtn_0e_6_usa
Change the name of the State where id = 2 to New Mexico
"""
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
    # state = session.query(State).where(State.id ==2).
    # update({state.name:'New Mexico'})
    session.query(State).filter(State.id == 2).update(
        {State.name: 'New Mexico'})
    session.commit()
