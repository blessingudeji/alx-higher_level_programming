#!/usr/bin/python3
""" A class that defines a student."""


class Student:
    """Class representation."""

    def __init__(self, first_name, last_name, age):
        """Initializes the class.
            """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """representation of the student class.
        """
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__
