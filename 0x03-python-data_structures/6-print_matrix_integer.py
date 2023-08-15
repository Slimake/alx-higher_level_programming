#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    length = len(matrix[0])
    if length != 0:
        for i in range(0, length):
            for j in range(0, length):
                if (j < length - 1):
                    print("{:d}".format(matrix[i][j]), end=" ")
                else:
                    print("{:d}".format(matrix[i][j]))
    else:
        print()
