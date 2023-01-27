#!/usr/bin/python3
def raise_exception_msg(message=""):
    my_name = "Angel"
    if not type(my_name) is int:
        raise NameError(message)
