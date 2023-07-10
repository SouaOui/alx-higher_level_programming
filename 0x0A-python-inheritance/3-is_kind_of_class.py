#!/usr/bin/python3
"""
returns True if the object is an instance of, or if the object is
an instance of a class that inherited from,
the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """check if obj is of type(a_class) or inherit form"""
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    return False
