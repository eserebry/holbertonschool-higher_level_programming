#!/usr/bin/python3
"""
adds the State object “Louisiana” to the database via SQLAlchemy
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

    new_state = State(id=6, name='Louisiana')
    session.add(new_state)
    session.commit()
    print("{}" .format(new_state.id))
    session.close
