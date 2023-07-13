#!/usr/bin/python3
"""
write an object to a file using json represenation
"""
import json


def save_to_json_file(my_obj, filename):
    """write json to filename"""
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
