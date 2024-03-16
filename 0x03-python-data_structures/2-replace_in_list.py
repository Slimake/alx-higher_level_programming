#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at a specific position
        Args:
            my_list: a list
            idx: index
            element: value to replace an element in a list

        Returns:
            The return value. my_list
        """
    if my_list:
        # Return original list if idx is negative
        if idx < 0:
            return my_list
        # Return original list if idex is out of range
        if idx > len(my_list) - 1:
            return my_list
        else:
            # Cycle through list, stop at index and modify element
            my_list[idx] = element
            # Return the modified list
            return my_list
