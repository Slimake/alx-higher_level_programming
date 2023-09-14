#!/usr/bin/python3
"""
8-rectangle module

Contains Rectangle class that inherits from BaseGeometry class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines Rectangle class that inherit form BaseGeometry class"""
    def __init__(self, width, height):
        """Initializes the class instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
