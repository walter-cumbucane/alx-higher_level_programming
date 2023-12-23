#!/usr/bin/python3
"""
    A script that inserts a row in a database using sqlalchemy
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


def main():
    """
        Main Function
    """
    username = argv[1]
    password = argv[2]
    database = argv[3]

    conn = f"mysql://{username}:{password}@localhost:3306/{database}"
    engine = create_engine(conn)
    Session = sessionmaker(bind=engine)

    session = Session()
    obj = State("Lousiana")
    session.add(obj)
    session.commit()
    print(obj.id)
    session.close()


if __name__ == "__main__":
    main()
