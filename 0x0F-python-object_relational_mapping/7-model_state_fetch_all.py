#!/usr/bin/python3
"""
Module list all State objects from the database
"""

import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    # Establish Connection with DB
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database
    query = session.query(State).order_by(State.id)
    for state in query.all():
        print("{:d}: {:s}".format(state.id, state.name))

    session.close()
