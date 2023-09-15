#!/usr/bin/python3
"""
100-my_int module.

Contains MyInt class that is a subclass of int class.
"""


class MyInt(int):
    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return True

    def __str__(self):
        return super().__str__()
