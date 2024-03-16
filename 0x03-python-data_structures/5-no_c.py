#!/usr/bin/python3
def no_c(my_string):
    """Removes all characters c and C from a string
        and return new string

        Args:
            my_string: a string

        Returns:
            The return value. new string
        """
    new_string = ""
    # Cycle through the string
    for char in my_string:
        # Check if char is c or C
        if char not in 'cC':
            # concatenate only if char is not c or C
            new_string += char
    return new_string
