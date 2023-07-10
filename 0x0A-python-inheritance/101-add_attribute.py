#!/usr/bin/python3

def add_attribute(obj, attr_name, attr_value):
    """add attribute and raise error"""
    if hasattr(obj, '__dict__'):
        obj.__dict__[attr_name] = attr_value
    else:
        raise TypeError("Can't add new attribute")
