#!/usr/bin/python3
"""This module contains a function that adds two integers"""


def add_integer(a, b=98):
    """This function adds two integers
    Args:
        a (int):
        b (int):
    Returns:
        The sum of a and b

    Raises:
        TypeError: If a or b is not an integer
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
