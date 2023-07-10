#!/usr/bin/python3
"""define add attribute"""


def add_attribute(obj, attr_name, attr_value):
    """add attribute and raise error"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("Can't add new attribute")
    setattr(obj, attr_name, attr_value)
