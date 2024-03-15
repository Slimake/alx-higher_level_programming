#!/usr/bin/python3


def element_at(my_list, idx):
    """Retrieves an element from a list

        Args:
            my_list: a list
            idx: index

        Returns:
            The return value. None if negatvie or an element if positive
        """
    # check if idx is negative or out of range
    if idx < 0 or idx > len(my_list) - 1:
        return None
    return my_list[idx]
