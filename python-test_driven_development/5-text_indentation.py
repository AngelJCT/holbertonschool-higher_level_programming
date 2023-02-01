#!/usr/bin/python3
"""
This module contains a function that prints a
text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    This function prints a text with 2
    new lines after each of these characters: ., ? and :
    Args:
        text (str): text to print
    Returns:
        Nothing
    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if len(text) == 0:
        raise TypeError("text_indentation() missing 1 \
            required positionalargument: 'text'")
    for i in range(len(text)):
        if text[i] in ['.', '?', ':']:
            print(text[i])
            print()
        elif text[i] == ' ' and text[i - 1] in ['.', '?', ':']:
            continue
        else:
            print(text[i], end='')
