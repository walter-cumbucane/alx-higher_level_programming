#!/usr/bin/python3
"""This module contains a function"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a file using the JSON representation"""
    with open(filename, "w") as json_file:
        json.dump(my_obj, json_file)
