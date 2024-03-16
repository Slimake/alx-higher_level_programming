#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific position in a list

        Args:
            my_list: a list

        Returns:
            The return value. list
        """
    # if idx is negative or out of range, return my_list
    if (idx < 0) or (idx > len(my_list) - 1):
        return my_list
    # Delete item
    del my_list[idx]
    # return list
    return my_list
