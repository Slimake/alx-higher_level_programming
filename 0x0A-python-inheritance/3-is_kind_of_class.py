#!/usr/bin/python3
"""
Module 3-is_kind_of_class.py
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if an object is an instance a class that's
    inherited through the specificed class otherwise false.
    """
    return isinstance(obj, a_class)
