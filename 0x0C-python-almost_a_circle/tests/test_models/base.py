#!/usr/bin/python3
"""This module contains the definition of a Base class"""


class Base(object):
    """Defines a Base class"""

    """Defines a public class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class's constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
