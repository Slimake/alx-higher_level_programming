#!/usr/bin/python3
"""
Module 3-say_my_name contains a function that

prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
        Prints My name is <first name> <last name>
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {0:s} {1:s}".format(first_name, last_name))
