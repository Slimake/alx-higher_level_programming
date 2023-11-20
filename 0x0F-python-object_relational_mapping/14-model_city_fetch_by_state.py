#!/usr/bin/python3
"""
Module prints all cities and states
"""
import sys
from model_state import Base, State
from model_city import City
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
    query = session.query(State.name, City.id, City.name).filter(
        State.id == City.state_id).order_by(
        City.id)

    for row in query.all():
        print("{:s}: ({:d}) {:s}".format(row[0], row[1], row[2]))

    session.close()
