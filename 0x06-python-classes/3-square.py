#!/usr/bin/python3
"""This code defines a Square class"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    Methods:
        area: returns the square area
    """
    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """calculates the square's area
        Args:
            None
        Returns:
            The square's area
        """
        area = self.__size * self.__size
        return area
