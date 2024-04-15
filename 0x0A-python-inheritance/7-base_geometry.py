#!/usr/bin/python3
"""
Module 7-base_geometry.py
"""


class BaseGeometry:
    """
    Defines public instance method area and
    public instance method integer_validator
    """
    def area(self):
        """
        Computes area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates integer
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
