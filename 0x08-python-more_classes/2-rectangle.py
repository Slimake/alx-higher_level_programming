#!/usr/bin/python3
"""
Module 2-rectangle

Defines class Rectangle
"""


class Rectangle:
    """
    Defines class Rectangle.

    with private instance attribute width, height
    and private instance method area, perimeter.

    Args:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
    """
    def __init__(self, width, height):
        """Initialize the instance of class Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of a rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)