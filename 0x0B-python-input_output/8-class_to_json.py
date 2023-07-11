#!/usr/bin/python3
"""JSON class function"""


def class_to_json(obj):
    """returns the dictionary description"""
    return (obj.__dict__)
