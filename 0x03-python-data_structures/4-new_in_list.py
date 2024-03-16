#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Check if my_list is empty
    if my_list:
        # Return my_list if idx is negative
        if idx < 0:
            return idx
        # Return my_list if idx is out of range
        if idx > len(my_list) - 1:
            return idx
        else:
            my_list_copy = my_list.copy()
            # Cycle through my_list
            for i in range(len(my_list_copy)):
                # If idx matches i
                if i == idx:
                    my_list_copy[i] = element
            return my_list_copy
