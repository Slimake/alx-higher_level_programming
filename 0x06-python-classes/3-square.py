#!/usr/bin/python3
"""
3-square module
Declares class sqaure with private attribute size, also raises an exception
"""


class Square:
    """
    class definition

    Args:
        size (int): size of the square.
    """
    def __init__(self, size=0):
        """
        The __init__ method defines a data attribute and
        raises an exception if size is not an integer.

        Attributes:
            size (int): size of the square,
            default value of 0 if no size passed.
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Returns current square area

        Returns:
            area
        """
        return (self.__size * self.__size)
