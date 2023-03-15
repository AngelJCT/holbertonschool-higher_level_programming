#!/usr/bin/python3
"""Module 10-model_state_my_get"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    """Print the State object with the name passed as argument"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{database}"
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    names = session.query(State).filter(State.name == state_name)
    result = names.all()
    for state in result:
        print(state.id)
    if not result:
        print("Not found")
    session.close()
