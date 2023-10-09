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
