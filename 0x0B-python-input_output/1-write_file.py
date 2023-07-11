#!/usr/bin/python3
"""
read the file
"""


def write_file(filename="", text=""):
    """read the file"""
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
