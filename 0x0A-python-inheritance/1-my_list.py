#!/usr/bin/python3
"""
1-my_list module

This module contains a class MyList that inherits from list
"""


class MyList(list):
    """
    Defines MyList class that inherits from list class.
    """
    def __init__(self):
        """Initialize the object instance"""
        super().__init__(self)

    def print_sorted(self):
        print(sorted(self))
