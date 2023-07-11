#!/usr/bin/python3
"""
read the file
"""


def read_file(filename=""):
    """read the file"""
    with open("filename", encoding="utf-8") as file:
        print(file.read())
