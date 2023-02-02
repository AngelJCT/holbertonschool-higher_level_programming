#!/usr/bin/python3
"""This module contains a function that prints a square"""


def print_square(size):
    """This function prints a square
    Args:
        size (int): size of the lenght of the square

    Returns:
        Nothing

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
        TypeError: size must be an integer
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
