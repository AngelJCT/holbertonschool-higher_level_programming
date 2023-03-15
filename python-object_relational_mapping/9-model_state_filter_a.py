#!/usr/bin/python3
"""Module 9-model_state_filter_a"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    """lists all State objects that contain the letter a from hbtn_0e_6_usa"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://user:{username}:{password}@localhost/{database}"
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).order_by(State.id).filter(State.name.contains('a'))
    names = state.all()
    for result in names:
        print(f"{result.id}: {result.name}")
    session.close()
