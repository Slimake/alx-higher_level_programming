#!/usr/bin/python3
"""
Module 101-locked class

Defines LockedClass
"""


class LockedClass:
    """
    Defines a class that prevents a user from dynamically create new instance
    attributes.
    """
    __slots__ = ["first_name"]
