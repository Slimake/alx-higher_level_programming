#!/usr/bin/python3
def remove_char_at(str, n):
    str_copy = str[:]
    result = ""
    for index, char in enumerate(str_copy):
        if not index == n:
            result += char
    return result
