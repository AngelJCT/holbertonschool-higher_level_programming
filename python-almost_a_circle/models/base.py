#!/usr/bin/python3
"""Module 0-base.py"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return Json string representation"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
