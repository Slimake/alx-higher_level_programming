#!/usr/bin/python3
"""
Module 4-inherits_from.py
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class
    that inherits (directly or indirectly) from the specified class
    otherwise False
    """
    return type(obj) is not a_class and issubclass(obj.__class__, a_class)
