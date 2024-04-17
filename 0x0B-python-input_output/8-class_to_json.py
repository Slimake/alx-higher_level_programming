#!/usr/bin/python3
"""
8-class_to_json module

Contains a function that returns the dictionary description with simple
data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object:
"""


def class_to_json(obj):
    """Returns the dictionary description"""
    return obj.__dict__
