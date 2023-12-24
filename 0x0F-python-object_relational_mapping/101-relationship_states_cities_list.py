#!/usr/bin/python3
"""
    Implementing database operations using sqlalchemy
"""
from relationship_city import City
from relationship_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def main():
    """
        Main Function
    """
    conn = f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(conn)
    Session = sessionmaker(bind=engine)

    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
        cities = session.query(City, State).join(State)
        cities = cities.filter(City.state_id == state.id).all()
        for city, state in cities:
            print(f"\t{city.id}: {city.name}")

    session.close()


if __name__ == "__main__":
    main()
