#!/usr/bin/python3
"""
This script lists all State objects that contain letter 'a' from the database hbtn_0e_6_usa.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    if len(argv) < 4:
        exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    filtered_states = session.query(State).filter(State.name.like('%a%')).order_by(State.id)

    for state in filtered_states:
        print('{}: {}'.format(state.id, state.name))
