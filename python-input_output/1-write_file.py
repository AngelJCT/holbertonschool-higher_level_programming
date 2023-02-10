#!/usr/bin/python3
"""Module 1-write_file"""


def write_file(filename="", text=""):
    """Function to write text to a file"""
    with open(filename, "w", encoding='utf-8') as my_file:
        my_file.write(text)
        return len(text)
