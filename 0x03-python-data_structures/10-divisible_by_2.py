#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list

        Args:
            my_list: a list

        Returns:
            The return value. list
        """
    # Check if my_list is empty
    if my_list:
        new_list = []
        # Cycle through my_list
        for i in my_list:
            # If i is a multiple of 2, return True else False
            if i % 2 == 0:
                new_list.append(True)
            else:
                new_list.append(False)
        return new_list
