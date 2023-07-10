#!/usr/bin/python3
"""
Create A SubClass of List
"""


class MyList(list):
    """Create MyList class"""

    def print_sorted(self):
        """print list in order ascending"""
        list_t = self[:]
        list_t.sort()
        print(list_t)
