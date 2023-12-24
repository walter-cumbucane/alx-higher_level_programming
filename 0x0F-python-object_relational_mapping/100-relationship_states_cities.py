#!/usr/bin/python3
"""
    A script that introduces table relationships in databases
    using sqlalchemy
"""

from relationship_city import City
from relationship_state import State, Base
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
    Base.metadata.create_all(engine)

    session = Session()
    obj1 = State(name="California")
    session.add(obj1)
    session.commit()
    obj2 = City(name="San Francisco", state_id=obj1.id)
    session.add(obj2)
    session.commit()


if __name__ == "__main__":
    main()
