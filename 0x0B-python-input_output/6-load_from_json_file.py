#!/usr/bin/python3
"""
6-load_from_json_file module.

Contain a function that creates an Object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file"""
    with open(filename, encoding="utf-8") as a_file:
        json_string = a_file.read()
        python_data = json.loads(json_string)
        return python_data
