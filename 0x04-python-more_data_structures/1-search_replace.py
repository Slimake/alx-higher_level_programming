#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """ Replaces all occurrences of an element by another in a new list

        Args:
            my_list: initial list
            search: the element to replace in the list
            replace: the new element

        Returns:
            The return value. new list
        """
    # Check if the list is not empty
    if my_list:

        # Make new copy of my_list
        new_list = my_list[:]

        # Cycle through my_list
        for i in range(len(new_list)):
            # If element at index is same as search, replace
            if new_list[i] == search:
                new_list[i] = replace

        return new_list
