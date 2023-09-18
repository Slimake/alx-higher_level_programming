#!/usr/bin/python3
"""
rectangle module

Contains Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """Define Rectangle class that inherit from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the class instance

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
            x (int): x coordinate
            y (int): y coordinate
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")

        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")

        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")

        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints a rectangle using '#'"""
        for row in range(self.__y):
            print("")

        for row in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """
        Update the data attributes, using a list of args(*args)
        or keyworded arguments(**kwargs) is passed
        """
        if args:
            for count, arg in enumerate(args):
                if count == 0:
                    self.id = args[0]
                elif count == 1:
                    self.__width = args[1]
                elif count == 2:
                    self.__height = args[2]
                elif count == 3:
                    self.__x = args[3]
                elif count == 4:
                    self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value

    def __str__(self):
        """print [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return ("[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".
                format(self.__class__.__name__, self.id,
                       self.__x, self.__y, self.__width, self.__height))

    def to_dictionary(self):
        """Return dictionary representation of a rectangle"""
        dt = {}
        dt['id'] = self.id
        dt['width'] = self.width
        dt['height'] = self.height
        dt['x'] = self.x
        dt['y'] = self.y
        return dt
