#!/usr/bin/python3
"""
Module 8-rectangle.py
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
