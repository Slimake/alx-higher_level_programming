#!/usr/bin/python3
"""Module 6-load_from_json_file.py
"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file
    """
    with open(filename, "r", encoding="utf-8") as my_file:
        py_obj = json.loads(my_file.read())
        return py_obj
