#!/usr/bin/python3
"""Module 11-student"""


class Student():
    """Class for student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation of student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retreives dictionary representation of Student instance"""
        if isinstance(attrs, list) and all(
            isinstance(elements, str) for elements in attrs
        ):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance"""
        for k, v in json.items():
            self.__dict__[k] = v
