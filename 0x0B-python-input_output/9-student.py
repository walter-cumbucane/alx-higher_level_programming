#!/usr/bin/python3
"""This module contains a class"""


class Student(object):
    """Defines a student class"""

    def __init__(self, first_name, last_name, age):
        """class's constructor"""
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of the object"""
        return self.__dict__
