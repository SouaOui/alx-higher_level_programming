#!/usr/bin/python3
"""
Create a Subclass of List
"""


class MyList(list):
    """Create MyList class"""

    def print_sorted(self):
        """Print the list in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
