#!/usr/bin/python3
"""
Module 1-my_list.py
"""


class MyList(list):
    """
    Inherits list attributes and methods
    """
    def print_sorted(self):
        """
        Prints the list but sorted(ascending order)
        """
        print(sorted(self))
