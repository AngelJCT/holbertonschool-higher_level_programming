#!/usr/bin/python3
"""Module Rectangle that inherits from Base"""

from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if type(value) is not int and type(self.__width) is not int:
            raise TypeError("width must be an integer")
        if self.__width <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if type(value) is not int and type(self.__height) is not int:
            raise TypeError("height must be an integer")
        if self.__height <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        if type(self.__x) is not int and type(value) is not int:
            raise TypeError("x must be an integer")
        if self.__x < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        if type(self.__y) is not int and type(value) is not int:
            raise TypeError("y must be an integer")
        if self.__y < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
