#!/usr/bin/python3
"""
101-add_attribute module

Contains a function that adds new attribute to an object if possible
"""


def add_attribute(obj, key, value):
    """Adds a new attribute to an object"""
    if '__dict__' in dir(obj):
        obj.__setattr__(key, value)
    else:
        raise TypeError("can't add new attribute")
        
