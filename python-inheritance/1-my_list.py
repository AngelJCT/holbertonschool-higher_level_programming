#!/usr/bin/python3
"""Module 1-my_list"""


class MyList(list):
    """MyList class that inherits from list."""
    def print_sorted(self):
        """Print the list, but sorted (ascending sort)."""
        print(sorted(self))
