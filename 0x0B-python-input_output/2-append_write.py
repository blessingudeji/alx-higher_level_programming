#!/usr/bin/python3
"""A function that appends a string"""


def append_write(filename="", text=""):
    """appends a string at the end of a text"""
    with open(filename, "a", encoding='utf=8') as newfile:
        return(newfile.write(text))
