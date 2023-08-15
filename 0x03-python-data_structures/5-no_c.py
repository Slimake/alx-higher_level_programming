#!/usr/bin/python3
def no_c(my_string):
    alt_str = ""
    for i in my_string:
        if i not in "cC":
            alt_str += i
    return alt_str
