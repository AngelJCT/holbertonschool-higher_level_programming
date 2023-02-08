#!/usr/bin/python3
"""Module 4-inherits_from"""


def inherits_from(obj, a_class):
    """Chekcs if an object is an isntance of a class that inherited
    from a class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
