#!/usr/bin/python3
"""This module contains only a function"""


def inherits_from(obj, a_class):
    """Object is an instance of a subclass of the specified class"""
    class_name = type(obj)
    if issubclass(class_name, a_class) and class_name != a_class:
        return True
    else:
        return False
