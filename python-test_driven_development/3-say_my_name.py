#!/usr/bin/python3
"""This module contains a function that prints a name"""


def say_my_name(first_name, last_name=""):
    """This function prints a name
    Args:
        first_name (str): The first name
        last_name (str): The last name

    Returns:
        Nothing

    Raises:
        TypeError: If first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if len(first_name) == 0 and len(last_name) == 0:
        raise TypeError("say_my_name() missing 1 required positional argument: 'first_name'")
    print(f"My name is {first_name} {last_name}")
