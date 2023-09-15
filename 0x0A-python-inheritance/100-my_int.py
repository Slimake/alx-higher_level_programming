#!/usr/bin/python3
"""
100-my_int module.

Contains MyInt class that is a subclass of int class.
"""


class MyInt(int):
    """Define MyInt class which is a subclass of int class"""
    def __init__(self, num) -> None:
        self.num = num

    def __eq__(self, other):
        """Invert __eq__ operator"""
        return self.num != other

    def __ne__(self, other):
        """Invert __ne__ operator"""
        return self.num == other

    def __str__(self):
        """print to screen"""
        return super().__str__()
