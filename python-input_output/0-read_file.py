#!/usr/bin/python3
"""Module 0-read_file"""


def read_file(filename=""):
    """Function to read file"""
    with open(filename, encoding="utf-8") as f:
        read_file = f.read()
    print(read_file)
