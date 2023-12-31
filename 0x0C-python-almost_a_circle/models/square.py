#!/usr/bin/python3
"""
square module

Contains the square function that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines Square class that inherits from Rectangle

    Methods:
        __init__(self, x=0, y=0, id=None):
        size(self)
        size(self, value)
        __str__(self)
        update(self, *args, **kwargs)
        to_dictionary(self)

    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the class instance

        Args:
            size (int): size of the square
            x (int): x coordinate poisition
            y (int): y coordinate poisition
            id (int): id
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the data attributes"""
        if args:
            for index, value in enumerate(args):
                if index == 0:
                    self.id = value
                elif index == 1:
                    self.size = value
                elif index == 2:
                    self.x = value
                elif index == 3:
                    self.y = value
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def __str__(self):
        """print [Square] (<id>) <x>/<y> - <size>"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.size)

    def to_dictionary(self):
        """Return dictionary representation of a square"""
        dt = {}
        dt["id"] = self.id
        dt["size"] = self.size
        dt["x"] = self.x
        dt["y"] = self.y
        return dt
