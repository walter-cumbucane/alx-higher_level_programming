#!/usr/bin/python3
"""Contains a function"""


def add_attribute(obj, attribute, value):
    """ add_attribute function """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    if not hasattr(obj, attribute):
        obj.__setattr__(attribute, value)
