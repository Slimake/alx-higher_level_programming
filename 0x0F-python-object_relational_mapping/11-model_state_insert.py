#!/usr/bin/python3
"""
Module adds the State object 'Louisiana to the database
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

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add state and save to database
    session.add(State(name="Louisiana"))
    session.commit()

    # Query database for states that contains letter 'a'
    query = session.query(State).order_by(State.id)
    for row in query.all():
        pass
    print("{:d}".format(row.id))

    session.close()
