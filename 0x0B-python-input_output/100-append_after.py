#!/usr/bin/python3
"""Defines a text file insertion function."""

def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file
    after a line containing that specifc string
    """
    text = ""
    with open(filename, "r", encoding='utf-8') as file1:
        for line in file1:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w", encoding="utf-8") as file2:
        file2.write(text)
