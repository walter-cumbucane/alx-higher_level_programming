#!/usr/bin/python3
"""
    This scripts queries through a database using the sqlalchemy library
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def main():
    """
        Main Function
    """
    user_name = argv[1]
    password = argv[2]
    database = argv[3]

    conn = f"mysql://{user_name}:{password}@localhost:3306/{database}"
    engine = create_engine(conn)
    Session = sessionmaker(bind=engine)

    session = Session()
    rows = session.query(State).filter(State.name.like('%a%'))
    rows = rows.order_by(State.id.asc()).all()
    for state in rows:
        print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    main()
