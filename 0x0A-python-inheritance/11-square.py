#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:

    def area(self):
        """raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value for positive integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""rectangle class"""


class Rectangle(BaseGeometry):
    """creates the rectangle class"""
    def __init__(self, width, height):
        """initializes the rectangle"""
        if not super().integer_validator("width", width):
            self.__width = width
        if not super().integer_validator("height", height):
            self.__height = height

    def area(self):
        """returns an area"""
        return self.__width * self.__height

    def __str__(self):
        """returns a string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


"""square class"""


class Square(Rectangle):
    """creates a square"""

    def __init__(self, size):
        """initializes the rectangle"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """returns the string of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
