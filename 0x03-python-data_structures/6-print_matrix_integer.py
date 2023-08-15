#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for j in row:
            if j is not row[len(row) - 1]:
                print("{:d}".format(j), end=" ")
            else:
                print("{:d}".format(j), end="")
        print()
