#!/usr/bin/python3
"""
Module 9-rectangle.py
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Constructor for class instance
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Return area of a rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        return ("[{}] {}/{}".format(type(self).__name__, self.__width,
                self.__height))
