#!/usr/bin/python3
"""
    A script that updates a record in a database using sqlalchemy
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


def main():
    """
        Main Function
    """
    conn = f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(conn)
    Session = sessionmaker(bind=engine)

    session = Session()
    row = session.query(State).filter(State.id == 2).first()
    if row:
        row.name = "New Mexico"
        session.commit()
    session.close()


if __name__ == "__main__":
    main()
