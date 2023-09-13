#!/usr/bin/python3
"""
1-my_list module

This module contains a class MyList that inherits from list
"""


class MyList(list):
    """
    Defines MyList class that inherits from list class.
    """
    def print_sorted(self):
        """Prints the list, but sorted(ascending order)"""
        print(sorted(self))
