#!/usr/bin/python3
"""
Student class.
"""


class Student:
    """Class representation."""
    def __init__(self, first_name, last_name, age):
        """Initializes the class."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary representation of the class"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for x in attrs:
            try:
                new_dict[x] = self.__dict__[x]
            except FileNotFoundError:
                pass
        return new_dict

    def reload_from_json(self, json):
        """replaces all attributes."""
        for key in json:
            try:
                setattr(self, key, json[key])
            except FileNotFoundError:
                pass
