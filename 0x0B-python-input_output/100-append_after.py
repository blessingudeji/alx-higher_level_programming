#!/usr/bin/python3
"""A function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """appends after a line"""
    with open(filename, mode='r', encoding='utf-8') as newfile:
        lines = newfile.readlines()

    with open(filename, mode='w', encoding='utf-8') as newfile:
        for line in lines:
            newfile.write(line)
            if search_string in line:
                newfile.write(new_string)
