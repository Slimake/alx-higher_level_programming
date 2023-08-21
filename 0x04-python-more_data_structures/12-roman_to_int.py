#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    if roman_string == "":
        return 0

    roman_dict = \
        {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}
    result = 0
    for i, j in zip(roman_string, roman_string[1:]):
        if roman_dict[i] >= roman_dict[j]:
            result += roman_dict[i]
        elif roman_dict[i] <= roman_dict[j]:
            result -= roman_dict[i]
    result += roman_dict[roman_string[-1]]
    return result
