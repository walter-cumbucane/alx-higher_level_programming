#!/usr/bin/python3
"""This module contains a class that inherits the list class"""


class MyList(list):
    """Inherits from the list class"""

    def __init__(self):
        """Constructor"""
        super().__init__()

    def print_sorted(self):
        """Prints the object in ascending order"""
        self.sort()
        print(self)
