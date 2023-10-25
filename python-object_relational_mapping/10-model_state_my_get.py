#!/usr/bin/python3
"""This is a script for listing the first State object in a database """

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
import sys


def fetch_states():
    """ Fetches all State objects"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    state = session.query(State).filter_by(name=sys.argv[4]).first()
    if state:
        print(f"{state.id}")
    else:
        print("Not found")
    session.close()


if __name__ == "__main__":
    fetch_states()
