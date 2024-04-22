#!/usr/bin/python3
""" rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Rectangle Constructor
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width
        """
        self.__width = value

    @property
    def x(self):
        """ Getter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x
        """
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
        self.__y = value
