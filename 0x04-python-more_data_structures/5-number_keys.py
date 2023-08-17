#!/usr/bin/python3
def number_keys(a_dictionary):
    if a_dictionary is not None:
        count = 0
        for k in a_dictionary.keys():
            count += 1
        return count
    return None
