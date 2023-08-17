#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is not None:
        result = 0
        my_list = list(set(my_list))
        for i in my_list:
            result += i
        return result
    return None
