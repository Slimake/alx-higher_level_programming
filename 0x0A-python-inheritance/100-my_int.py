#!/usr/bin/python3
"""
Module 100-my_int.py
"""


class MyInt(int):
    """
    Class MyInt that inherits from int
    """
    def __init__(self, num):
        """Contructor"""
        self.num = num

    def __eq__(self, other):
        """Equal magic method"""
        return self.num != other

    def __ne__(self, other):
        """Not equal magic method"""
        return self.num == other
