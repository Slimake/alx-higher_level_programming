#!/usr/bin/python3
""" rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes the class instance.

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
            x (int): x coordinate
            y (int): y coordinate
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """ Returns the area value of the Rectangle instance
        """
        return self.width * self.height

    def display(self):
        """ Prints character # to the stdout using x and y coordinate
        """
        print("\n" * self.y, end="")
        for line in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute
        """
        if args:
            for index, arg in enumerate(args):
                if index == 0:
                    self.id = arg
                elif index == 1:
                    self.width = arg
                elif index == 2:
                    self.height = arg
                elif index == 3:
                    self.x = arg
                elif index == 4:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of class Rectangle
        """
        obj = {}
        obj['id'] = self.id
        obj['width'] = self.width
        obj['height'] = self.height
        obj['x'] = self.x
        obj['y'] = self.y
        return obj

    @property
    def width(self):
        """ Getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __str__(self):
        """ String representation of Rectangle class
        """
        return ("[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                    type(self).__name__, self.id, self.x,
                    self.y, self.width, self.height))
