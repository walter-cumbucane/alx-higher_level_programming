#!/usr/bin/python3
"""
    Contains a script that queries on a database using sqlalchemy
"""
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def main():
    """
        The main function
    """
    conn = f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(conn)
    Session = sessionmaker(bind=engine)

    session = Session()
    state = session.query(State).order_by(State.id.asc()).first()
    print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    main()
