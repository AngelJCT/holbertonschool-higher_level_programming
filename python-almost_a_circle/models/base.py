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

    @classmethod
    def save_to_file(cls, list_objs):
        """Write json string representation to a file"""
        if list_objs is None:
            list_objs = []
        tjs = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(f"{cls.__name__}.json", 'w', encoding='utf-8') as f:
            f.write(tjs)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the json string representation"""
        if json_string is None:
            return []
        return json.loads(json_string)
