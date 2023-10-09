#!/usr/bin/python3
"""Implements an int's subclass"""


class MyInt(int):
    """Implements a rebel int's subclass"""

    def __init__(self, value):
        """Class's constructor"""
        self.__value = value
        super().__init__()

    def __eq__(self, other):
        """Handles the '=' operator"""
        return self.__value != other

    def __ne__(self, other):
        """Handles the '!=' operator"""
        return self.__value == other
