#!/usr/bin/python3
"""
10-square module

Contains Square class that inherits from Rectangle class which inherit
from BaseGeometry class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines Square class that inherit from Rectangle class
    which inherit from BaseGeometry
    """
    def __init__(self, size):
        """Initializes the class instance

        Args:
            size (int): the size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
