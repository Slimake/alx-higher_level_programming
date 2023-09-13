#!/usr/bin/python3
"""
2-append_write module.

Contains append_write function that appends a string at the end of a
text file and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file.

    returns the number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as a_file:
        a_file.write(text)
        return len(text)
