#!/usr/bin/python3
"""
deletes all State objects with a name containing the letter a
from the database via SQLAlchemy
"""
import MySQLdb
import sys
from model_state import Base, State
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

    state_del = session.query(State).filter(State.name.contains('a')).all()
    for state in state_del:
        session.delete(state)
    session.commit()
    session.close
