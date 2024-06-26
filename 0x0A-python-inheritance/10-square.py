#!/usr/bin/python3
"""
Module 10-square.py
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Class Square that inherits from Rectangle
    """
    def __init__(self, size):
        """Constructor for class instance

        Args:
            size (int): the size of the square
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
