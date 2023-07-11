#!/usr/bin/python3
"""A function that writes an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file, using json rep"""
    with open(filename, mode='w', encoding='utf-8') as newfile:
        newfile.write(json.dumps(my_obj))
