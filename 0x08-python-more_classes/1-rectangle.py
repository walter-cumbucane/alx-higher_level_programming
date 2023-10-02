#!/usr/bin/python3
"""This module creates a Rectangle class"""


class Rectangle:
    """Represents a rectangle
    Attributes:
        __height (int): height of the rectangle
        __width (int): width of the rectangle
    Methods:
        None
    """
    def __init__(self, width=0, height=0):
        """initializes the square
        Args:
            __width (int): height of the rectangle
            __height (int): height of the rectangle
        Returns:
            None
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.width

    @width.setter
    def width(self, value):
        """width setter"""
