#!/usr/bin/python3
"""This module defines a Class Square"""


class Square:
    """This class defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """This method initializes the class Square"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """This method returns the current size"""
        return self.__size

    @size.setter
    def size(self, value):
        """This method sets the current square size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """This function returns the current position"""
        return self.__position

    @position.setter
    def position(self, value):
        """This function set the value"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """This method returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """This function prints the size in #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
