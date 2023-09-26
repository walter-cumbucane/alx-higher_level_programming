#!/usr/bin/python3
"""This code defines a Square class"""


class Square:
    """This is the class's constructor"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
