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
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"
