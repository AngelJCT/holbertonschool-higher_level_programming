#!/usr/bin/python3
"""Module 2-is_same_class"""


def is_same_class(obj, a_class):
    """Function to check if an objet is an instance of a specified class"""
    if type(obj) is a_class:
        return True
    else:
        return False
