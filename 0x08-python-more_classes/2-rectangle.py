#!/usr/bin/python3
"""
2-rectangle module

Defines Rectangle class
"""


class Rectangle:
    """Defines class Rectangle with private attribute width and height.

    Attributes:
        width (int): width of a rectangle
        height (int): height of a rectangle
    """

    def __init__(self, width=0, height=0):
        """Initializea a rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter sets width if value >= 0"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter gets height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter sets height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns width * height"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns 2 * (width + height) if width or height is not 0"""
        if self.__width == 0 or self.height == 0:
            return 0
        return 2 * (self.__width + self.__height)
