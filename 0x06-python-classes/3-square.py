#!/usr/bin/python3
"""Contains Square class that defines a square"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initializes the instance of Square class"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = int(size)

    def area(self):
        return self.__size * self.__size
