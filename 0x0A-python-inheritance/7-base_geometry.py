#!/usr/bin/python3
"""
7-base_geometry module.

Contains BaseGeometry class and area function that raises an exception.
"""


class BaseGeometry:
    """Defines BaseGeometry class"""
    def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Defines integer_validator class that validates an integer"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
