#!/usr/bin/python3
"""
1-Square Module
Defines class Square with private attribute size
"""


class Square:
    """Class Square definition"""
    def __init__(self, size):
        """
        An init method that defines a private data attribute

        Args:
            size: size of the square
        """
        self.__size = size
