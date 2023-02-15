#!/usr/bin/python3
"""Module 0-base.py"""


import json
from os import path


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

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    def update(self, *args, **kwargs):
        """Update the instance attributes"""
        attributes = ['id', 'width', 'height', 'size', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @classmethod
    def load_from_file(cls):
        """Return a list of instances"""
        if not path.exists(f"{cls.__name__}.json"):
            return []
        with open(f"{cls.__name__}.json", 'r', encoding='utf-8') as f:
            lff = [cls.create(**obj) for obj in cls.from_json_string(f.read())]
            return lff
