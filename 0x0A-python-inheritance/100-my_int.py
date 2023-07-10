#!/usr/bin/python3
"""Create a class that inherit from int """


class MyInt(int):
    """invert this two operators"""

    def __eq__(self, other):
        """is equal"""
        return self.real != other

    def __ne__(self, other):
        """not equal"""
        return self.real == other
