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
        f"mysql+mysqldb://{username}:{password}@localhost/{database}"
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    states = (
        session.query(State)
        .filter(State.name.like("%a%"))
        .order_by(State.id)
        )
    results = states.all()
    for state in results:
        print(f"{state.id}: {state.name}")
    session.close()
