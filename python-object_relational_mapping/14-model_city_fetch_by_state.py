#!/usr/bin/python3
"""Module 14-model_city_fetch_by_state"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    """Print all City objects from database hbtn_0e_14_usa"""
    username = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{database}"
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    objects = session.query(City, State)\
        .filter(City.state_id == State.id)\
        .order_by(City.id)
    for city, state in objects:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
