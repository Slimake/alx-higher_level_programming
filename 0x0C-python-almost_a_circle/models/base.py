#!/usr/bin/python3
""" base Module
"""
import json


class Base:
    """ Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Base constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries
        """
        if not list_dictionaries:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string
        """
        if not json_string:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file
        """
        instance = []

        if list_objs:
            for obj in list_objs:
                instance.append(obj.to_dictionary())

        json_str = cls.to_json_string(instance)

        filename = cls.__name__ + ".json"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(3, 4)
        elif cls.__name__ == "Square":
            dummy = cls(5)

        dummy.update(**dictionary)

        return dummy
