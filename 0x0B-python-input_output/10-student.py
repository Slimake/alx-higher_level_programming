#!/usr/bin/python3
"""
9-student module

Contains Student class
"""


class Student:
    """This class defines a Student class.

    It defines the init method and the to_json method.
    """
    def __init__(self, first_name, last_name, age):
        """This initializes the object instance.

        Args:
            first_name (str): first name of the student.
            last_name (str): last name of the student.
            age (int): age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This returns the public instance dictionary.

        Args:
            attrs: A list of strings

        Returns:
            self.__dict__ if no attrs, otherwise return new_dict
        """
        new_dict = {}

        if attrs is not None:
            for name in attrs:
                if self.__dict__.__contains__(name):
                    new_dict[name] = self.__dict__[name]
            return new_dict
        else:
            return self.__dict__
