#!/usr/bin/python3
"""
BaseGeometry and Rectangle class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representation of a rectangle"""
    def __init__(self, width, height):
        """initializes of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
