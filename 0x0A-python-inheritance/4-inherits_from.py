#!/usr/bin/python3
"""
Direct inherit or indirectly
"""


def inherits_from(obj, a_class):
    """ inherits (yes/No) Directly or Inderctly"""
    return isinstance(obj, a_class) and not type(obj) is a_class
