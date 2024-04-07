#!/usr/bin/python3
"""
Module 0-add_integer contains a function that adds two integers

Returns the addition of the two integers
"""


def add_integer(a, b=98):
    """
        Returns the addition of two integers
    """
    if (not type(a) in (float, int)):
        raise TypeError("a must be an integer")
    if (not type(b) in (float, int)):
        raise TypeError("b must be an integer")
    return int(a + b)
