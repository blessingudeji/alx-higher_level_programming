#!/usr/bin/python3
"""A function that creates an object from a JSON file"""

import json

def load_from_json_file(filename):
    """creates the object from a Json file"""
    with open(filename, mode='r', encoding='utf-8') as newfile:
        return json.load(newfile)
