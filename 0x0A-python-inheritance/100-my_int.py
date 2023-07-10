#!/usr/bin/python3
"""Create a class that inherit from int """


class MyInt(int):
    def __eq__(self, other):
        """is equal"""
        return super().__ne__(other)

    def __ne__(self, other):
        """not equal"""
        return super().__eq__(other)
