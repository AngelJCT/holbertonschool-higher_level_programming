#!/usr/bin/python3
"""Module 10-square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Subclass of Rectangle"""
    def __init__(self, size):
        self.__size = size
        super().integer_validator("size", size)

    def area(self):
        """Method that defines the area of square"""
        return self.__size ** 2

    def __str__(self):
        """Method that prints rectangle description"""
        return (f"[Rectangle] {self.__size}/{self.__size}")
