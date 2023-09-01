#!/usr/bin/python3
"""
101-square module
Declares class sqaure with private attribute size, position using a getter
 and setter, also raises an exception, print '#' self.__size number of times
"""


class Square:
    """
    class definition

    Args:
        size (int): size of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        The __init__ method defines a data attribute and
        raises an exception if size is not an integer.

        Attributes:
            size (int): size of the square,
            default value of 0 if no size passed.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter

        Returns:
            int: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter

        Args:
            size: the size of the area if size in int and >= 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2 or \
            type(value[0]) is not int or type(value[1]) is not int or \
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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

        Also print space using position
        """
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

        # Another way to print the '#' character
        # print("\n" * self.__position[1], end="")
        # print("\n".join([" " * self.__position[0]
        #                 + '#' * self.__size for row in range(self.__size)]))
    def __str__(self):
        """
        String representation of an instance
        """
        hash = ""
        if self.__size == 0:
            return hash

        hash += "\n" * self.__position[1]
        hash += "\n".join([" " * self.__position[0]
                           + '#' * self.__size for row in range(self.__size)])
        return hash
