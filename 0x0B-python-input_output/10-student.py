#!/usr/bin/python3
""" Student class module
"""


class Student:
    """ Student class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if not attrs:
            return self.__dict__
        else:
            new_dict = {}
            for name in attrs:
                try:
                    new_dict[name] = self.__dict__[name]
                except KeyError:
                    continue
            return new_dict
