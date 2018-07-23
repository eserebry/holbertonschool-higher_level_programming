#!/usr/bin/python3
"""
prints all City objects from the database via SQLAlchemy
"""
import MySQLdb
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    city_print = session.query(City, State).join(State)\
                .filter(State.id == City.state_id)\
                .order_by(City.id).all()
    for cities, states in city_print:
        print("{}: {} {}" .format(states.name, cities.id, cities.name))
    session.close()
