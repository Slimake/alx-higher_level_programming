#!/usr/bin/python3
"""
4-inherits_from module

Contains a function that True if the object is an instance of a class that
inherited (directly or indirectly) from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Returns True

    if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False.
    """
    return type(obj) is not a_class
