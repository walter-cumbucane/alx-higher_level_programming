#!/usr/bin/python3
"""This module implements a square method"""
base_class = __import__("9-rectangle").Rectangle


class Square(base_class):
    """Implements a square class"""
    def __init__(self, size):
        """class's constructor"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
