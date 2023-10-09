#!/usr/bin/python3
"""This module checks if an object is part of a class or not"""


def is_same_class(obj, a_class):
    """Checks whether an object is an instance of a class or not"""
    if type(obj) is a_class:
        return True
    else:
        return False
