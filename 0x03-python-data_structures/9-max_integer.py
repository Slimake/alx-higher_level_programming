#!/usr/bin/python3
def max_integer(my_list=[]):
    """Finds the biggest integer of a list

        Args:
            my_list: a list
        Returns:
            The return value. int
        """
    # set first item in the list to maxi
    maxi = my_list[0]
    # If my_list is empty return None
    if not my_list:
        return None
    # Cycle through my_list
    for num in my_list:
        if maxi < num:
            maxi = num
    return maxi
