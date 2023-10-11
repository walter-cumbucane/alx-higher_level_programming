#!/usr/bin/python3
"""This module contains a function"""
import json


def to_json_string(my_obj):
    """Encodes an object into json string format"""
    json_data = json.dumps(my_obj)
    return json_data
