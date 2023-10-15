#!/usr/bin/python3
from models.base import Base
"""This modules contains a Rectangle class that inherits from Base"""


class Rectangle(Base):
    """Defines a Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class's constructor"""
        super().__init__(id)
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be >= 0")
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be >= 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x <= 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y <= 0:
            raise ValueError("y must be >= 0")
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

    """Height getter"""
    @property
    def height(self):
        return self.__height

    """Height setter"""
    @height.setter
    def height(self, value):
        self.__height = value

    """X getter"""
    @property
    def x(self):
        return self.__x

    """X setter"""
    @x.setter
    def x(self, value):
        self.__x = value

    """Y getter"""
    @property
    def y(self):
        return self.__y

    """Y setter"""
    @y.setter
    def y(self, value):
        self.__y = value
