#!/usr/bin/python3
def weight_average(my_list=[]):
    """Returns the weighted average of all integers tuple"""
    if my_list:
        tuple_sum = 0
        last_item = 0
        # Cycle through my_list
        for row in my_list:
            # Sum and store the tuple element in my_list
            tuple_sum += row[0] * row[1]
            # Store the last item in the tuple
            last_item += row[-1]
        # Divide the stored sum and the last item
        # of each tuple in my_list and return
        return tuple_sum / last_item
    else:
        return 0
