#!/usr/bin/python3
"""This module defines a Class Square"""


class Square:
    """This class defines a square"""

    def __init__(self, size=0):
        """This function initializes the square"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """This function returns the current square area"""
        return self.__size ** 2
