#!/usr/bin/python3
"""add_attribute function"""


def add_attribute(obj, attr, value):
    """adds new attribute to the object"""
    if('__slots__' in dir(obj) or '__dict__' not in dir(obj) or
       hasattr(obj, attr)):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
