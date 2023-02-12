#!/usr/bin/python3
"""Module 0-base.py"""


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation of Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
