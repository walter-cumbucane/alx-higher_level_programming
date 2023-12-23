#!/usr/bin/python3
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


print("Everything imported")

conn = "mysql://walter:my_password@localhost:3306/alx"
engine = create_engine(conn)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

session = Session()
try:
    object1 = State(name="California")
    print("Done")
except Exception as e:
    print(e)

session.add(object1)
session.commit()
session.close()
