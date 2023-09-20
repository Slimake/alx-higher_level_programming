#!/usr/bin/python3
"""
base module

Contains the base class for all other classes
"""
import json


class Base:
    """Defines the Base class

    Attributes:
        __nb_objects = 0

    Methods:
        __init__(self, id=None)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the class instance

        Args:
            id (int): attribute of the class instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation

        Args:
            list_dictionaries (dict): a list of dictionaries
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes json string representation of list_objs to file"""
        obj = []

        if list_objs is not None:
            for o in list_objs:
                obj.append(cls.to_dictionary(o))
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(obj))

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(5, 5)
        elif cls.__name__ == "Square":
            dummy = cls(5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        lis = []
        filename = cls.__name__ + ".json"
        try:
            with open(filename, encoding="utf-8") as file:
                json_string = file.read()

                new_list = cls.from_json_string(json_string)
                for obj in new_list:
                    lis.append(cls.create(**obj))
        except FileNotFoundError:
            pass
        return lis
