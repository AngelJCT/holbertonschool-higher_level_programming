#!/usr/bin/python3
def print_last_digit(number):
    last_digit = number % 10 # get last digit
    if last_digit < 0: # if negative, make positive
        last_digit *= -1
    print("{:d}".format(last_digit), end="") # print last digit
    return last_digit # return last digit
