#!/usr/bin/python3
"""
    This module contains a model definition
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer


class State(Base):
    """
        State Class Definition
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))

    def __init__(self, name):
        """
            Class's Constructor
        """
        self.name = name
