#!/usr/bin/python3


def print_list_integer(my_list=[]):
    if my_list:
        # Cycle through my_list
        for value in my_list:
            # Print each value per line
            print("{0}".format(value))
