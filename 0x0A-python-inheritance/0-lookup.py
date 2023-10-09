#!/usr/bin/python3
"""This module contains a function that returns the list of available   attributes and methods of an object"""

def lookup(obj):
    """This function receives an object as argument and returns a
    list of all available attributes and methods"""
    lst = list()
    lst = dir(obj)
    return lst
