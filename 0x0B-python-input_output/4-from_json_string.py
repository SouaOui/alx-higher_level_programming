#!/usr/bin/python3
"""
Json representation returns object
"""
import json


def from_json_string(my_str):
    """returns an object python data structure"""
    return json.loads(my_str)
