#!/usr/bin/python3
"""
Module prints State object with the name passed as argument
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

    # Query database for states that contains letter 'a'
    query = session.query(State).filter(State.name == sys.argv[4])
    row = query.first()
    if row:
        print(row.id)
    else:
        print("Not found")
    session.close()
