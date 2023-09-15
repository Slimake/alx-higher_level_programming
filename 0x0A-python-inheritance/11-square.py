#!/usr/bin/python3
"""
11-square module

Contains
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines"""
    def __init__(self, size):
        """Initializes the class instance
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Display"""
        return "[{:s}] {:d}/{:d}"\
            .format(self.__class__.__name__, self.__size, self.__size)
