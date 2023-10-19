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
                json_file.write(json_string)
            return

        list_dictionaries = list()
        print("About to create the list of dictionaries")
        for obj in list_objs:
            dictionary = obj.to_dictionary()
            list_dictionaries.append(dictionary)

        json_string = Base.to_json_string(list_dictionaries)
        with open(filename, "w") as json_file:
            json_file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Converts a json_string back to an usual python object"""
        if json_string is None or len(json_string) == 0:
            return []
        usual_data = json.loads(json_string)
        return usual_data

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        class_name = cls.__name__
        if class_name == "Rectangle":
            dummy = cls(1, 1, 1, 1, 1)
            dummy.update(**dictionary)
        elif class_name == "Square":
            dummy = cls(1, 1, 1, 1)
            dummy.update(**dictionary)
        else:
            dummy = cls()
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a json file"""
        filename = cls.__name__ + ".json"
        objects = list()
        try:
            with open(filename, "r") as json_file:
                json_string = json_file.read()
        except FileNotFoundError as e:
            return []
        usual_data = Base.from_json_string(json_string)
        for dictionary in usual_data:
            objects.append(cls.create(**dictionary))
        return objects
