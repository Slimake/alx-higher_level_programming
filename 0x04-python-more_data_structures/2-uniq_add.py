#!/usr/bin/python3
def uniq_add(my_list=[]):
    """ Adds all unique integers in a list

        Args:
            my_list: list

        Returns:
            The return value is. integer
        """
    # Check if my_list is empty
    if my_list:
        # Use the sum function, pass in set,
        # which takes my_list as argument
        return sum(set(my_list))
