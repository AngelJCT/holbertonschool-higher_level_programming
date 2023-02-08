#!/usr/bin/python3
"""Module 6-base_geometry"""


class BaseGeometry():
    """Empty class"""

    def area(self):
        """Method to raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to validate value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
