#!/usr/bin/python3
"""Module 9-student"""


class Student():
    """Class for student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation of student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retreives dictionary representation of Student instance"""
        return self.__dict__
