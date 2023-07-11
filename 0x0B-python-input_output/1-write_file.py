#!/usr/bin/python3
"""
A function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """Returns the number of character written"""
    with open(filename, 'w', encoding='utf=8') as newfile:
        return newfile.write(text)
