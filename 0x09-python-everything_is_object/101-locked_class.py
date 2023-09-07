#!/usr/bin/python3
"""
101-locked_class module
Defines a LockedClass
"""


class LockedClass(object):
    """
    Defines LockedClass

    A locked class that uses __slots__ to prevent users from /
    dynamically create new instance attributes
    """
    __slots__ = ['first_name']
