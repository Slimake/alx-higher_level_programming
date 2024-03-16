#!/usr/bin/python3
def multiple_returns(sentence):
    """Returna a tuple with the length of a string and its first character

        Args:
            sentence: string
        Returns:
            The return value. tuple
        """
    # if sentence is empty(falsy) return None
    if not sentence:
        return (0, None)
    return (len(sentence), sentence[0])
