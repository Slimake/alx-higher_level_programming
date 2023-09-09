#!/usr/bin/python3
"""
4-print_square module

prints a square with the character '#'
"""


def print_square(size):
    """
    prints a square with the character '#' if size > 0 and
    size is an integer, otherwise raise appropriate Exception
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print('#' * size)
