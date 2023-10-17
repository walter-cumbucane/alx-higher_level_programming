#!/usr/bin/python3
"""
    This module contains a Square class
"""
from models.square import Square


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

    def to_dictionary(self):
        """Returns the instance as a dictionary"""
        attributes = self.__dict__
        size = self.width
        x = self.x
        y = self.y
        del attributes['_Rectangle__width']
        del attributes['_Rectangle__height']
        del attributes['_Rectangle__x']
        del attributes['_Rectangle__y']
        attributes['x'] = x
        attributes['size'] = size
        attributes['y'] = y
        return attributes
