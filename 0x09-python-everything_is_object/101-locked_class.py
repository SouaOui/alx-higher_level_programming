#!/usr/bin/python3
"""
Module for class that prevents dynamic creation
of attributes
"""


class LockedClass():
    """create a class """
    __slots__ = ["first_name"]
