#!/usr/bin/python3
"""
2-matrix_divided module

Divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Takes an argument matrix and Divides all elements in the matrix
    """
    new_list = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        sub_list = []
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix \
                                (list of lists) of integers/floats")
            num = num / div
            sub_list.append(round(num, 2))
        new_list.append(sub_list)
    return new_list
