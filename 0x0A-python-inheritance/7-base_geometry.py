#!/usr/bin/python3
"""This module contains a BaseGeometry class"""


class BaseGeometry(object):
    """empty class"""

    def __init__(self):
        "Constructor"
        super().__init__()

    def area(self):
        """Calculates the area of the geometric figure"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A public instance method"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
