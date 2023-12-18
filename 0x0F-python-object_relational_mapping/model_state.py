#!/usr/bin/python3
"""
This script defines a State class and
a Base class to work with MySQLAlchemy ORM.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer


class State(Base):
    """State class

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The State id of the class
        name (str): The State name of the class

    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        """
            Class's Constructor
        """
        self.name = name
