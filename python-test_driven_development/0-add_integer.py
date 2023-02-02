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
    
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(1.5, 2.5)
    4
    >>> add_integer(1.5, 2)
    3
    >>> add_integer(50, "hello")
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    >>> add_integer(50, [1, 2, 3])
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    >>> add_integer((1, 2), 50)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    >>> add_integer(50, {1: 2})
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    >>> add_integer(50, None)
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    >>> add_integer(50, float('inf'))
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    >>> add_integer(0, 0)
    0
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
