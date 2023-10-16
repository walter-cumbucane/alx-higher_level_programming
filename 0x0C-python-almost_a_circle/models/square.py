#!/usr/bin/python3
from models.rectangle import Rectangle
"""This module contains a Square class"""


class Square(Rectangle):
    """Defines a Square class inherits from the Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class's constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Creates a printable object"""
        printable1 = f"[Square] ({self.id}) {self.x}/{self.y} "
        printable2 = f" - {self.width}"
        printable = printable1 + printable2
        return printable

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the instance's attributes"""
        if len(args) == 0:
            for key in kwargs:
                self.__setattr__(key, kwargs[key])
        else:
            for i in range(len(args)):
                if i >= 4:
                    break
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.width = args[1]
                    self.height = args[1]
                    self.size = args[1]
                elif i == 2:
                    self.x = args[2]
                elif i == 3:
                    self.y = args[3]
