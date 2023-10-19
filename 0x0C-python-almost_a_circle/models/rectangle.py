#!/usr/bin/python3
"""
    This modules contains a Rectangle class that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
        class Rectangle implements Base.
        Methods:
            __init__()
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Initializes the instance of the class..
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
            getter function for __width
            Returns: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            setter function for width.
            Args:
                value (int): value to be set.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
            getter function for height
            Returns: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            setter function for height
            Args:
                value (int): value to be set.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
            getter function for x.
            Returns: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            setter function for x.
            Args:
                value (int): value to be set.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
            getter function for y
            Returns: y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            setter function for y
            Args:
                value (int): value to be set.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
            Returns the area value of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
            Prints the rectangle in the stdout using the '#' symbol
        """
        to_print = str()
        for i in range(self.__height):
            to_print += (" " * self.x) + ("#" * self.width) + "\n"
        print(to_print, end="")

    def __str__(self):
        """
            Creates a printable string
        """
        printable1 = f"[Rectangle] ({self.id}) {self.__x}/{self.__y} "
        printable2 = f"- {self.__width}/{self.__height}"
        printable = printable1 + printable2
        return printable

    def update(self, *args, **kwargs):
        """
            Updates the class's attributes
        """
        if len(args) == 0:
            for key in kwargs:
                self.__setattr__(key, kwargs[key])
        else:
            for i in range(len(args)):
                if i >= 5:
                    break
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.width = args[1]
                elif i == 2:
                    self.height = args[2]
                elif i == 3:
                    self.x = args[3]
                elif i == 4:
                    self.y = args[4]

    def to_dictionary(self):
        """
            Returns the dictionary representation of a Rectangle
        """
        dictionary = {"x": self.x, "y": self.y}
        dictionary["height"] = self.height
        dictionary["width"] = self.width
        return dictionary
