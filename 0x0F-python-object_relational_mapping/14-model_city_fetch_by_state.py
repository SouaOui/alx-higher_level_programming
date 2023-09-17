#!/usr/bin/python3
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
    cities = session.query(City).order_by(City.id)
    if cities:
        for city in cities:
            print(f"{city.state.name}: ({city.id}) {city.name}")
