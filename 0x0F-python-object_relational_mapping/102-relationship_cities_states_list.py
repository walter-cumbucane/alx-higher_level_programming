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
    rows = session.query(City, State).join(City)
    rows = rows.filter(City.state_id == State.id).order_by(City.id.asc()).all()
    for city, state in rows:
        print(f"{city.id}: {city.name} -> {state.name}")
    session.close()


if __name__ == "__main__":
    main()
