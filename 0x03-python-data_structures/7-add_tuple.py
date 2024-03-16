#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples

        Args:
            tuple_a = first tuple
            tuple_b = second tuple

        Returns:
            The return value. a tuple
        """
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
