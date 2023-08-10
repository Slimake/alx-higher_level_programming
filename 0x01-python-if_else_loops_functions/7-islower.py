#!/usr/bin/python3


def islower(c):
    """Check for lowercase, return True if found or false if not found."""
    dec = ord(c)

    for i in range(97, 123):
        if i is dec:
            return True
    else:
        return False
