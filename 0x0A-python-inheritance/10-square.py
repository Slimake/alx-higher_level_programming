#!/usr/bin/python3
"""
10-square module

Contains Square class that inherits from Rectangle class which inherit
from BaseGeometry class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines Square class that inherit form Rectangle class"""
    def __init__(self, size):
        """Initializes the class instance

        Args:
            size (int): the size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculates and returns the area of a square"""
        return self.__size ** 2
