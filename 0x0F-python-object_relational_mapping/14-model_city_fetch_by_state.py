#!/usr/bin/python3
"""
This script lists all City objects from the database hbtn_0e_6_usa.
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    cities_and_states = session.query(City, State).join(State)

    for city, state in cities_and_states.order_by(City.id).all():
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    session.commit()
    session.close()
