#!/usr/bin/python3
"""myInt class module"""


class MyInt(int):
    """New instance of class"""

    def __init__(self, value):
        """initializes the class"""
        self.value = value

    def __eq__(self, a):
        """equals to method"""
        return self.value != a

    def __ne__(self, a):
        """not equal to method"""
        return self.value == a
