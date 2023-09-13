#!/usr/bin/python3
"""
4-from_json_string module

Contains the function that returns an object(Python data structure)
represented by a JSON string
"""
import json


def from_json_string(my_str):
    """Returns an object(Python data structure)"""
    return json.loads(my_str)
