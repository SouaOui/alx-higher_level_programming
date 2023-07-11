#!/usr/bin/python3
"""
Load an object from JSON file
"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a JSON file"""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
