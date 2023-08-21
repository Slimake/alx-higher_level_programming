#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        key = ''
        value = 0
        for k, v in a_dictionary.items():
            if v > value:
                key = k
                value = v
        return key
    return None
