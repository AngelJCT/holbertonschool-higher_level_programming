#!/usr/bin/python3
"""This module defines a Class Square"""


class Square:
    """This class defines a square"""

    def __init__(self, size=0):
        """This function initializes the square"""
        self.__size = size
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(size) is not int:
            raise TypeError("size must be an integer")
