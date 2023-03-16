#!/usr/bin/python3
"""Module 13-model_delete_a"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    """Delete all State objects with a name containing the letter a"""
    username = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{database}"
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(State).filter(State.name.like("%a%")).delete()
    session.commit()
    session.close()
