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

    def area(self):
        """This method gets the current area"""
        return self.__width * self.__height

    def perimeter(self):
        """This method gets the current perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """This method returns the current rectangle"""
        result = ""
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                result += "#" * self.__width
                if i != self.__height - 1:
                    result += "\n"
        return result

    def __repr__(self):
        """This method returns a string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"
