#!/usr/bin/python3
from models.base import Base
"""This modules contains a Rectangle class that inherits from Base"""


class Rectangle(Base):
    """Defines a Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class's constructor"""
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x <= 0:
            raise ValueError("x must be > 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y <= 0:
            raise ValueError("y must be > 0")
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """Width getter"""
    @property
    def width(self):
        return self.__width

    """Width setter"""
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    """Height getter"""
    @property
    def height(self):
        return self.__height

    """Height setter"""
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    """X getter"""
    @property
    def x(self):
        return self.__x

    """X setter"""
    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be > 0")
        self.__x = value

    """Y getter"""
    @property
    def y(self):
        return self.__y

    """Y setter"""
    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """Returns the area value of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints the rectangle in the stdout using the '#' symbol"""
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """Creates a printable string"""
        printable1 = f"[Rectangle] ({self.id}) {self.__x}/{self.__y} "
        printable2 = f"- {self.__width}/{self.__height}"
        printable = printable1 + printable2
        return printable

    def update(self, *args, **kwargs):
        """Updates the class's attributes"""
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
        """Returns the dictionary representation of a Rectangle"""
        dictionary = {"x": self.x, "y": self.y}
        dictionary["height"] = self.height
        dictionary["width"] = self.width
        return dictionary
