#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Replaces or adds key/value in a dictionary

        Args:
            a_dictionary: dict
            key: dict key
            value: dick value

        Returns:
            The return value. a_dictionary
        """
    # set the value to a_dictionary[key]
    a_dictionary[key] = value

    return a_dictionary
