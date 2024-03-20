#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value

        Args:
            a_dictionary: dict

        Returns:
            The return value. key with the biggest value
        """
    # Check if a_dictionary is not None
    if a_dictionary:
        max_value = 0
        # Cycle through a_dictionary
        for key, value in a_dictionary.items():
            # Check if max_value is less than a_dictionary
            if max_value < value:
                max_value = value
                max_key = key
        return max_key
    else:
        return None
