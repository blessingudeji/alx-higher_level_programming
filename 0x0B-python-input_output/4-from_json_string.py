#!/usr/bin/python3
"""A function that returns an object"""
import json


def from_json_string(my_str):
    """returns new object represented by a json str"""
    return json.loads(my_str)
