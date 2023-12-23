#!/usr/bin/python3
"""
    Interacts with a database using sqlalchemy
"""
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
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
    try:
        rows = session.query(City, State).join(State).filter(City.state_id == State.id).all()
    except Exception as e:
        print(e)
    for instance in rows:
        print(f"{instance.name}: {instance.id} {instance.name}")
    session.close()


if __name__ == "__main__":
    main()
    
