#!/usr/bin/python3
"""
4-rectangle module

Define Rectangle class
"""


class Rectangle:
    """Define Rectangle class with private attributes width and height
    that prints character "#" if width and height is > 0.

    Attributes:
        width (int): width of a rectangle.
        height (int): height of a rectangle.
    """
    def __init__(self, width=0, height=0):
        """Initialise an instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter sets the width"""
        if not type(value) is int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter sets the height"""
        if not type(value) is int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns width * height"""
        return self.__width * self.__height

    def perimeter(self):
        """returns 2 * (width + height) if width and height is not 0"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """returns the rectangle with the character '#' \
        if width or height is not 0"""
        if self.__width == 0 or self.__height == 0:
            return str()
        else:
            return "\n".join(["#" * self.__width
                              for row in range(self.__height)])

    def __repr__(self):
        """returns the string representation of the rectangle \
        to be able to recreate a new instance by using eval()
        """
        return "Rectangle(" + str(self.__width) \
            + ", " + str(self.__height) + ")"
