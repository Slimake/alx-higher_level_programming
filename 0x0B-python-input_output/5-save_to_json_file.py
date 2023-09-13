#!/usr/bin/python3
"""
5-save_to_json_file module.

Contains function that writes an Object to text file,
using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to text file using a JSON representation"""
    with open(filename, mode="w", encoding="utf-8") as a_file:
        to_json_string = json.dumps(my_obj)
        a_file.write(to_json_string)
