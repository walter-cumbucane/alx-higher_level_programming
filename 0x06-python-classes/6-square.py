#!/usr/bin/python3
"""This code defines a Square class"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
        position(tuple): I don't yet what does it do
    Methods:
        area: returns the square area
    """
    def __init__(self, size=0, position=(0, 0)):
        """initializes the square
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        self.__size = size
        self.__position = position

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

    """position getter"""
    @property
    def position(self):
        return self.__position

    """position setter"""
    @position.setter
    def position(self, position):
        state = True
        for num in position:
            if num < 0:
                state = False
        if state:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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
