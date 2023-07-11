#!/usr/bin/python3
"""A function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Adds a new attribute to an object
    Args:
        obj: The object to add attribute to.
        att: The name of the attribute.
        value: The value of attribute.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
