#!/usr/bin/python3
"""
9-rectangle module

Define Rectangle class
"""


class Rectangle:
    """Define Rectangle class with private attributes width and height
    that prints character "#" if width and height is > 0.

    Attributes:
        width (int): width of a rectangle.
        height (int): height of a rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialise an instance"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            return "\n".join([str(self.print_symbol) * self.__width
                              for row in range(self.__height)])

    def __repr__(self):
        """returns the string representation of the rectangle \
        to be able to recreate a new instance by using eval()
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not (isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not (isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
