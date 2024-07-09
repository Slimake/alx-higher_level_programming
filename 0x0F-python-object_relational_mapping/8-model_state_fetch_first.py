#!/usr/bin/python3
"""Module print first State object in the database"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Establish connection with database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database for first state in DB
    first_obj = session.query(State).order_by(State.id).first()
    if first_obj:
        print("{:d}: {:s}".format(first_obj.id, first_obj.name))
    else:
        print("Nothing")

    session.close()
