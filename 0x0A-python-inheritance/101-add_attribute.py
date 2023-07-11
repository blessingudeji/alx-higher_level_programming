#!/usr/bin/python3
"""A function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Adds a new attribute to an object
    Args:
        obj: The object to which the attribute will be added
        att: The attribute's name
        value: The attribute's value
    Raises:
        TypeError: If the attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
