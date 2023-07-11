#!/usr/bin/python3
"""Inherits_from module"""


def inherits_from(obj, a_class):
    """returns true or false"""
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
