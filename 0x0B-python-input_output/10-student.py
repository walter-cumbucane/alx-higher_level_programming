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

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of the object"""
        if type(attrs) is list:
            to_return = dict()
            attributes = self.__dict__
            for key in attributes:
                if key in attrs:
                    to_return[key] = attributes[key]
            return to_return
        return self.__dict__
