#!/usr/bin/python3
from base import Base
"""This modules contains a Rectangle class that inherits from Base"""


class Rectangle(Base):
    """Defines a Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class's constructor"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    """Width getter"""
    @property
    def width(self):
        return self.__width

    """Width setter"""
    @width.setter
    def width(self, value):
        self.__width = value
