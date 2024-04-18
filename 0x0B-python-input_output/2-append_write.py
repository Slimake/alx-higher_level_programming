#!/usr/bin/python3
"""Module 2-append_write.py"""


def append_write(filename="", text=""):
    """
    Appends a string to a text file
    Returns the number of characters written
    """
    with open(filename, "a", encoding="utf-8") as my_file:
        return my_file.write(text)
