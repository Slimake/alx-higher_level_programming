#!/usr/bin/python3
"""
1-write_file module.

Contains write_file function that writes a string to a text file and
returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and return the number
    of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as a_file:
        a_file.write(text)

    with open(filename, encoding="utf-8") as a_file:
        return len(a_file.read())
