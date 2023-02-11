#!/usr/bin/python3
"""Module 10-student"""


class Student():
    """Class for student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation of student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retreives dictionary representation of Student instance"""
        if isinstance(attrs, list) and all(isinstance(elements, str) for elements in attrs):
            return {key: value for key, value in self.__dict__.items() if key in attrs}
        return self.__dict__
