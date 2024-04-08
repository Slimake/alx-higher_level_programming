#!/usr/bin/python3
"""
Module 5-rectangle

Defines class Rectangle
"""


class Rectangle:
    """
    Defines class Rectangle.

    with private instance attribute width, height
    and private instance method area, perimeter
    and implement __str__() special method

    Attributes:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
    """
    def __init__(self, width=0, height=0):
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
        """
        Return 2 * (self.__width + self.__height) if width or height is not 0
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Informal String representation of rectangle instance"""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join("#" * self.width for _ in range(self.height))

    def __repr__(self):
        """Official string representation of rectangle instance"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print Bye rectangle when an object is deleted"""
        print("Bye rectangle")
