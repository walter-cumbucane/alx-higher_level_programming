#!/usr/bin/python3
"""This module contains a function"""
import json


def load_from_json_file(filename):
    """Loads from a json file and converts the content to a python object"""
    with open(filename, "r") as json_file:
        python_loaded_object = json.load(json_file)
    return python_loaded_object
