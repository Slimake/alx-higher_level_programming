#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary

        Args:
            a_dictionary: dict
            key: key to delete in a_dictionary

        Returns:
            The return value. a_dictionary
        """
    # Check if key in a_dictionary
    if key in a_dictionary:
        # Delete a_dictionary key
        del a_dictionary[key]

    return a_dictionary
