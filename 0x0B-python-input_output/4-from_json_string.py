#!/usr/bin/python3
"""THIS MODULE CONTAINS A FUNCTION"""
import json


def from_json_string(my_str):
    """Converts a json format string back into its orgininal object"""
    python_object = json.loads(my_str)
    return python_object
