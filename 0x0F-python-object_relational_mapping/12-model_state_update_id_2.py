#!/usr/bin/python3
"""
Module update the name of State object
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

    # Update row in database
    query = session.query(State).filter(State.id == 2).first()
    query.name = "New Mexico"

    # Save changes to database
    session.commit()

    # Close session
    session.close()
