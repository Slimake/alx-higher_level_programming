#!/usr/bin/python3
"""Module 1-write_file.py"""

import os


def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as my_file:
        return my_file.write(text)
