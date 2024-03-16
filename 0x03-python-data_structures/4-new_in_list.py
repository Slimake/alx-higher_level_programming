#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Make a copy of my_list
    my_list_copy = my_list[:]

    # Check if my_list_copy is empty
    if my_list_copy:
        # Return my_list_copy if idx is negative
        if idx < 0:
            return idx
        # Return my_list_copy if idx is out of range
        if idx > len(my_list_copy) - 1:
            return idx
        else:
            # Change element in my_list_copy at idx
            my_list_copy[idx] = element
            return my_list_copy
