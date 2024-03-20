#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """ Computes the square value of all integers of a matrix

        Args:
            matrix: nested list

        Returns:
            The return value. nested list
        """
    # Check to see if matrix is empty
    if matrix:
        # Declare an empty matrix
        squared_matrix = []

        # Cycle through inner list and square values
        for row in matrix:
            inner_matrix = []
            for value in row:
                inner_matrix.append(value ** 2)
            squared_matrix.append(inner_matrix)

        return squared_matrix
