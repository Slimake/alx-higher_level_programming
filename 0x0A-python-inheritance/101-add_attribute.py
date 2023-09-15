#!/usr/bin/python3
"""
100-add_attribute module

Contains a function that adds new attribute to an object if possible
"""


def add_attribute(obj, attribute, value):
    """Adds a new attribute to an object"""
    if '__dict__' in dir(obj):
        setattr(obj, attribute, value)
    else:
        raise TypeError("Can't add new attribute")
