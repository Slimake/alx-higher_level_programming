#!/usr/bin/python3


def print_list_integer(my_list=[]):
    """ Prints all integers of a list

    Args:
        my_list: a list

    Returns:
        None
    """

    if my_list:
        # Cycle through my_list
        for num in my_list:
            # Print each value per line
            print("{:d}".format(num))
