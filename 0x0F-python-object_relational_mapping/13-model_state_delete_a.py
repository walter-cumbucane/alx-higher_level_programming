#!/usr/bin/python3
"""
    Delets records from a database using SQLAlchemy
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
    rows = session.query(State).filter(State.name.contain('a')).all()
    if rows:
        for instance in rows:
            session.delete(instance)
            session.commit()
    session.close()


if __name__ == "__main__":
    main()
