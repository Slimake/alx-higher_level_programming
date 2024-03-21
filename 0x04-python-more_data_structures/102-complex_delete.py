#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary"""
    a_dictionary_copy = a_dictionary.copy()
    for key, obj_value in a_dictionary_copy.items():
        if obj_value == value:
            del a_dictionary[key]
    return a_dictionary
