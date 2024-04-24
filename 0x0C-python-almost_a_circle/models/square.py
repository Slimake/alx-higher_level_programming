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

    def update(self, *args, **kwargs):
        """ Update Rectangle instance attributes
        """
        if args:
            for index, arg in enumerate(args):
                if index == 0:
                    self.id = arg
                elif index == 1:
                    self.size = arg
                elif index == 2:
                    self.x = arg
                elif index == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square class
        """
        obj = {}
        obj['id'] = self.id
        obj['size'] = self.size
        obj['x'] = self.x
        obj['y'] = self.y
        return obj

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
