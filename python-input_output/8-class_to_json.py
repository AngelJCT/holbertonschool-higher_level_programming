#!/usr/bin/python3
"""Module 8-class_to_json"""


def class_to_json(obj):
    """return the dictionary description with simple data structure"""
    return obj.__dict__
