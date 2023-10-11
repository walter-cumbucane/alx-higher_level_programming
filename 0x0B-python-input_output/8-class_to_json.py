#!/usr/bin/python3
"""This module contains a function"""


def class_to_json(obj):
    """Returns a dict containning all attributes in key-value pairs"""
    attributes = obj.__dict__
    return attributes
