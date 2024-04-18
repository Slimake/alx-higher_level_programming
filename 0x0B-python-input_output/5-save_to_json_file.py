#!/usr/bin/python3
"""Module 5-save_to_json_file.py
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using JSON representation
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        my_file.write(json.dumps(my_obj))
