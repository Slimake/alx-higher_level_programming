#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_num = {"I": 1, "V": 5, "X": 10, "L": 50,
                 "C": 100, "D": 500, "M": 1000}
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    sum = 0
    for i, j in zip(roman_string, roman_string[1:]):
        if roman_num[i] >= roman_num[j]:
            sum += roman_num[i]
    elif roman_num[i] < roman_num[j]:
        sum -= roman_num[i]
    sum += roman_num[roman_string[-1]]
    return sum
