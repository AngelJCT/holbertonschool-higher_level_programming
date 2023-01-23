#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in reversed(my_list):
        if len(my_list) == 0:
            return
        else:
            print("{:d}".format(i))
