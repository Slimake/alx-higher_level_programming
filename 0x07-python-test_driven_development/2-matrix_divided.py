#!/usr/bin/python3
"""
Module 2-matrix-divided contains a function that

divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
        Divides all elements of a matrix
    """
    if type(matrix) is not list:
        raise TypeError(("matrix must be a matrix ") +
                        ("(list of lists) of integers/floats"))
    elif type(div) not in (int, float):
        raise TypeError("div must be a number")

    for row in matrix:
        # Check if each row is a list
        if type(row) is not list:
            raise TypeError(("matrix must be a matrix ") +
                            ("(list of lists) of integers/floats"))
        # Check if each element is int or float
        for j in row:
            if type(j) not in (int, float):
                raise TypeError(("matrix must be a matrix ") +
                                ("(list of lists) of integers/floats"))

    # Check if each row of the matrix is of the same size
    for row in matrix:
        # Get length of first row
        first_row_len = len(matrix[0])

        if not (len(row) == first_row_len):
            raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for i in matrix:
        new_inner_matrix = []
        for j in i:
            new_inner_matrix.append(round(j / div, 2))
        new_matrix.append(new_inner_matrix)
    return new_matrix
