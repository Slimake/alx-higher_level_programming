#!/usr/bin/python3
""" square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes the class instance.

        Args:
            size (int): the size of the square
            x (int): x coordinate
            y (int): y coordinate
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size
        """
        self.width = value
        self.height = value

    def __str__(self):
        """ String representation of Square class
        """
        return ("[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
                    type(self).__name__, self.id, self.x, self.y, self.width))
