#!/usr/bin/python3
"""This module implements a square method"""


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


class Rectangle(BaseGeometry):
    """Implements a rectangle class"""
    def __init__(self, width, height):
        """class's constructor"""
        super().__init__()
        super().integer_validator("height", height)
        super().integer_validator("width", width)
        self.__width = width
        self.__height = height

    def area(self):
        """implements the area's method"""
        return self.__width * self.__height

    def __str__(self):
        """To make the instance printable"""
        printable = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return printable


class Square(Rectangle):
    """Implements a square class"""
    def __init__(self, size):
        """class's constructor"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Implements the area method"""
        return self.__size ** 2

    def __str__(self):
        """Makes the instance printable"""
        printable = "[square] {:d}/{:d}".format(self.__size, self.__size)
        return printable
