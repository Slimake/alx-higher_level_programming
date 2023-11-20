#!/usr/bin/python3
"""
Module delete all State objects with a name that contains 'a'
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    # Establish connection with database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query database for states that contains letter 'a' and delete
    query = session.query(State).filter(State.name.like('%a%'))
    query.delete(synchronize_session='fetch')
    session.commit()

    session.close()
