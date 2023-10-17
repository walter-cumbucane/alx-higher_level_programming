#!/usr/bin/python3
"""This module contains the definition of a Base class"""
import json


class Base(object):
    """Defines a Base class"""

    """Defines a public class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class's constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of the argument"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        json_string = json.dumps(list_dictionaries)
        return json_string

    @classmethod
    def save_to_file(cls, list_objs):
        """Write json string representation of a list of objects to a file"""
        filename = cls.__name__ + ".json"

        if list_objs is None or len(list_objs) == 0:
            json_string = Base.to_json_string(list_objs)
            with open(filename, "w") as json_file:
                json_file.write(json_write)
            return

        list_dictionaries = list()
        for obj in list_objs:
            dictionary = obj.to_dictionary()
            list_dictionaries.append(dictionary)

        json_string = Base.to_json_string(list_dictionaries)
        with open(filename, "w") as json_file:
            json_file.write(json_string)
