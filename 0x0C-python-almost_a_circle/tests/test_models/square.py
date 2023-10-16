#!/usr/bin/python3
#from models.rectangle import Rectangle
from rectangle import Rectangle
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
