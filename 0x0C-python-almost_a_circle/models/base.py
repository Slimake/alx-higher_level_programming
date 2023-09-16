#!/usr/bin/python3
"""
base module

Contains the base class for all other classes
"""


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
