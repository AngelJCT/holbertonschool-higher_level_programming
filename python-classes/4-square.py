#!/usr/bin/python3
"""This module defines a Class Square"""


class Square:
    """This class defines a square"""

    def __init__(self, size=0):
        """This method initializes the class Square"""
        self.__size = size

    def area(self):
        """This method returns the current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """This method returns the current square size"""
        return self.__size

    @size.setter
    def size(self, value):
        "This method sets the current square size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
