#!/usr/bin/python3
"""This module contains a rectangle class"""
base_geometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(base_geometry):
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
