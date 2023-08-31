#!/usr/bin/python3
"""
5-square module
Declares class sqaure with private attribute size using getter and setter,
 also raises an exception, print '#' self.__size number of times
"""


class Square:
    """
    class definition

    Args:
        size (int): size of the square.
    """
    def __init__(self, size=0):
        """
        The __init__ method defines a data attribute and
        raises an exception if size is not an integer.

        Attributes:
            size (int): size of the square,
            default value of 0 if no size passed.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter

        Returns:
            int: size
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        setter

        Args:
            size: the size of the area if size in int and >= 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Returns current square area

        Returns:
            int: area
        """
        return (self.__size * self.__size)

    def my_print(self):
        """
        Prints the square with the character "#" self.__size times
        """
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)

        # Another way to print the '#' character
        # print("\n".join(['#' * self.__size for row in range(self.__size)]))
