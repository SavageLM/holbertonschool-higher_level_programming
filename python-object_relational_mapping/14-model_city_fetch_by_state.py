#!/usr/bin/python3
"""This is a script for listing all City objects in a database """

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
import sys


def fetch_cities():
    """ Fetches all City objects"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    rslt = session.query(State, City).filter(City.state_id == State.id).all()
    for state, city in rslt:
        print(f"{state.name}: ({city.id}) {city.name}")


if __name__ == "__main__":
    fetch_cities()
