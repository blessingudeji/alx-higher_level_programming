#!/usr/bin/python3
"""A class that defines a rectangle

"""


class Rectangle:
    """Initializing  rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """get width

        """
        return self.__width

    @property
    def height(self):
        """get height

        """
        return self.__height

    @width.setter
    def width(self, value):
        """set width

        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """set height

        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """returns the area of rectangle

        """
        return self.width * self.height

    def perimeter(self):
        """ returns the perimeter of rectangle

        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)
