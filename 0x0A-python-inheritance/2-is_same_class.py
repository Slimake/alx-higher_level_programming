#!/usr/bin/python3
"""
2-is_same_class module

Contains is_same_class function that returns True if the object
is exactly an instance of the specified class.
"""


def is_same_class(obj, a_class):
    """Returns True if object is exactly an instance of a class"""
    return type(obj) == a_class
