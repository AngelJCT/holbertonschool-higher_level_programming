#!/usr/bin/python3
"""Module 8-recangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Subclass derived from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)
