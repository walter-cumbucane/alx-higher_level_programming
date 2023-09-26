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
        self.__size = size

    """ size getter """
    @property
    def size(self):
        return self.__size

    """ size setter """

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """calculates the square's area
        Args:
            None
        Returns:
            The square's area
        """
        area = self.__size * self.__size
        return area

    def my_print(self):
        """prints the square in #
        Args:
            None
        Returns:
            None
        """
        if self.__size == 0:
            print("")
        else:
            i = 0
            while i < self.__size:
                for j in range(0, self.__size):
                    print("#", end="")
                i += 1
                print("")
