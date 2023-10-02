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
    number_of_instances = 0
    print_symbol = "#"

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
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes the rectangle's area"""
        return self.__width * self.__height

    def perimeter(self):
        """Computes the rectangle's perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Returns an unofficially string to be printed"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.__height):
            for j in range(self.__width):
                string += str(self.print_symbol)
            if i == self.__height - 1:
                break
            string += "\n"
        return string

    def __repr__(self):
        """Returns an officialy printable string"""
        string = "Rectangle({}, {})".format(self.__width, self.__height)
        return string

    def __del__(self):
        """Destructor"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """A static method that returns the biggest rectangle based
        on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area1 = rect_1.area()
        area2 = rect_2.area()
        if area1 < area2:
            return rect_2
        else:
            return rect_1
