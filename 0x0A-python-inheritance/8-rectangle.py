#!/usr/bin/python3
"""This module contains a rectangle class"""
base_geometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(base_geometry):
    """Implements a rectangle class"""
    def __init__(self, width, height):
        """class's constructor"""
        super().__init__()
        try:
            super().integer_validator("Rectangle", height)
        except Exception as e:
            raise TypeError("height must be an integer")
        try:
            super().integer_validator("Rectangle", width)
        except Exception as e:
            raise TypeError("width must be an integer")
        self.__width = width
        self.__height = height
