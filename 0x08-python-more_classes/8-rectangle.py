#!/usr/bin/python3
"""
Module 8-rectangle

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
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the instance of class Rectangle"""
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __str__(self):
        """Informal String representation of rectangle instance"""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(str(self.print_symbol)
                         * self.width for _ in range(self.height))

    def __repr__(self):
        """Official string representation of rectangle instance"""
        return "{}({}, {})". \
            format(self.__class__.__name__, self.width, self.height)

    def __del__(self):
        """Print Bye rectangle when an object is deleted"""
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")
