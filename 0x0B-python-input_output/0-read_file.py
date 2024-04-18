#!/usr/bin/python3
"""Module 0-read_file.py
"""

def read_file(filename=""):
    """Reads a text file and print it to stdout
    """
    with open(filename, encoding="utf-8") as myFile:
        for line in myFile:
            print(line, end="")
