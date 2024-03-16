#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers

        Args:
            matrix: a list
        Returns:
            The return value. None
        """
    # Check if matrix is empty
    if matrix:
        # Cycle through the row of matrix list
        for lst in matrix:
            # Cycle through the column of each inner list of matrix list
            for index, num in enumerate(lst):
                # print each element
                if not (index == len(lst) - 1):
                    print("{:d}".format(num), end=" ")
                else:
                    print("{:d}".format(num), end="")
            print()
