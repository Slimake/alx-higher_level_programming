#!/usr/bin/python3
"""Module 1-write_file.py"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file
    Returns the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        return my_file.write(text)
