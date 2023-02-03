#!/usr/bin/python3
"""This module define a class for a rectangle"""


class Rectangle():
    """This class define a rectangle"""

    def __init__(self, width=0, height=0):
        """This method initialize the class Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """This method returns the current width"""
        return self.__width

    @width.setter
    def width(self, value):
        """This method sets the current width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This method returns the current height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This method sets the current height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
