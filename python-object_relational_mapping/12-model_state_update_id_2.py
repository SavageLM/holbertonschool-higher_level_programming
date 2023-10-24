#!/usr/bin/python3
"""This is a script for listing the first State object in a database """

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
import sys


def update_states():
    """ updates a State objects"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    updated_state = session.query(State).filter_by(id=2).first()
    if updated_state:
        updated_state.name = "New Mexico"
        session.commit()
        print("State with id 2 has been updated to 'New Mexico'")
    session.close()


if __name__ == "__main__":
    update_states()
