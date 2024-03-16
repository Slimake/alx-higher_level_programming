#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list
        Args:
            my_list = a list

        Return:
            The return value. None
        """
    # If my_list is not empty
    if my_list:
        # Cycle through my_list
        for num in reversed(my_list):
            print("{:d}".format(num))
