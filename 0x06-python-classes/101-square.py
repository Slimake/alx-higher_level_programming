#!/usr/bin/python3
"""Contains Square class that defines a square"""


class Square:
    """Defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the instance of Square class"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position"""
        return self.__position

    @position.setter
    def position(self, pos):
        """Setter for position"""
        if (not isinstance(pos, tuple)) or (len(pos) != 2) or \
            (not isinstance(pos[0], int)) or (not isinstance(pos[1], int)) or \
                pos[0] < 0 or pos[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = pos

    def area(self):
        """Returnn area of a square"""
        return self.__size * self.__size

    def my_print(self):
        """Print space and # character"""
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for j in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    def __str__(self):
        """ Print space and # character """
        if self.__size == 0:
            return "\n"
        else:
            return (("\n" * self.__position[1]) +
                    ("\n".join([" " * self.__position[0] + '#' * self.__size
                                for row in range(self.__size)])))
