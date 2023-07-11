#!/usr/bin/python3
"""A function that returns json rep of objects"""
import json


def to_json_string(my_obj):
    """returns jjson representation of object"""
    return json.dumps(my_obj)
