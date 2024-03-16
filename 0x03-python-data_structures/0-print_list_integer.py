#!/usr/bin/python3


def print_list_integer(my_list=[]):
    if len(my_list):
        for value in my_list:
            print("{0:d}".format(value))
