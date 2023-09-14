#!/usr/bin/python3
"""
9-rectangle module

Contains Rectangle class that inherits from BaseGeometry class and
implement the area method
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines Rectangle class that inherit form BaseGeometry class"""
    def __init__(self, width, height):
        """Initializes the class instance

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Display the string to the screen"""
        return "[{}] {}/{}"\
            .format(self.__class__.__name__, self.__width, self.__height)

    def area(self):
        """Calculates and returns the area of a rectangle"""
        return self.__width * self.__height
