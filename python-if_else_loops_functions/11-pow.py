#!/usr/bin/python3
def pow(a, b):
    my_base = a
    my_exponent = b
    my_result = 1
    
    while my_exponent != 0:
        my_result *= my_base
        my_exponent -= 1
    return my_result
