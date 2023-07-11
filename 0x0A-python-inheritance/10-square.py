#!/usr/bin/python3
"""BaseGeometryclass"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """creates a square"""

    def __init__(self, size):
        """initializing rectangle"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
