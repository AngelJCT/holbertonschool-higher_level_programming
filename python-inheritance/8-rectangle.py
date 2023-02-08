#!/usr/bin/python3
"""Module 8-recangle"""


class BaseGeometry:
    """Class BaseGeometry"""
    def area(self):
        """Function to calculate the area of a shape"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function to validate the value of a shape"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Subclass derived from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)
