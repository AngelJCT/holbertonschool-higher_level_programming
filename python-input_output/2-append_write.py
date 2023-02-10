#!/usr/bin/python3
"""Module 2-append_write"""


def append_write(filename="", text=""):
    """Function to apppend text to a file"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
