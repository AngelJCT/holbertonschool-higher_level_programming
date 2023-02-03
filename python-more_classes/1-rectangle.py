#!/usr/bin/python3
"""This module define a class for a rectangle"""


class Rectangle():
    """This class define a rectangle"""
    def __init__(self, width=0, height=0):
        """This function initiate a rectangle width and height"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """This function gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """This function set the value of width"""
        if not isinstance(self.width, int):
            raise TypeError("width must be an integer")
        if self.width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This function gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This function set the value of height"""
        if not isinstance(self.height, int):
            raise TypeError("height must be an integer")
        if self.height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
