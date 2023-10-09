#!/usr/bin/python3
"""Contains a function that returns the list of all object's properties"""


def lookup(obj):
    """Returns all attributes and methods accesible by an object"""
    lst = list()
    lst = dir(obj)
    return lst
