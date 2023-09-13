#!/usr/bin/python3
"""
0-read_file module

Reads a text file and prints it to stdout.
"""


def read_file(filename=""):
    """
    Reads and print a text file to the stdout
    """
    with open(filename, mode='r', encoding="utf-8") as a_file:
        print(a_file.read())
