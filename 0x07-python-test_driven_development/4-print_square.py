#!/usr/bin/python3
"""
Module 4-print_square contains a function that

prints a square with the character #.
"""


def print_square(size):
    """
        Prints a square with the character #
    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    size = int(size)
    for i in range(size):
        print("#" * size)
