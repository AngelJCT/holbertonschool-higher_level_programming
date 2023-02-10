#!/usr/bin/python3
"""Module 4-from_json_string.py"""


import json


def from_json_string(my_str):
    """Returns an object represented by json string"""
    return json.loads(my_str)
