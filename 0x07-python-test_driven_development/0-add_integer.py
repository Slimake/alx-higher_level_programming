#!/usr/bin/python3
"""
0-add_integer module

Add two integers together
"""


def add_integer(a, b=98):
    """
    Adds two integer together only if a and b is floats or integers
    """
    if not type(a) in [int, float]:
        raise TypeError("a must be an integer")
    elif not type(b) in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
