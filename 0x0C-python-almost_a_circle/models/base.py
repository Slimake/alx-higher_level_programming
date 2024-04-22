#!/usr/bin/python3
""" base Module
"""


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
