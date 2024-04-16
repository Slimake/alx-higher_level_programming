#!/usr/bin/python3
"""
Module 101-add_attribute.py
"""


def add_attribute(obj, key, value):
    """
    Adds a new attributes to an object if it's possible
    """
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, key, value)
