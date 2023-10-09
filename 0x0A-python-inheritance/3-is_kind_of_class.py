#!/usr/bin/python3
"""This module contains just one function"""


def is_kind_of_class(obj, a_class):
    """Checks if the object is an instance of a class or its subclass    es"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
