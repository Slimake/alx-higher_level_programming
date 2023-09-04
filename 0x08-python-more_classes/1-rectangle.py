#!/usr/bin/python3
"""
1-rectangle module

Defines a Rectangle class
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """An init method that defines a private data attribute.

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """:int: value."""
        return self.__width
    
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise ValueError("widht must be >= 0")
        elif value < 0:
            raise TypeError("width must be an integer")
        else:
            self.__width = value
        
    @property
    def height(self):
        """:int: value."""
        return self.__height
    
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise ValueError("height must be >= 0")
        elif value < 0:
            raise TypeError("height must be an integer")
        else:
            self.__height = value