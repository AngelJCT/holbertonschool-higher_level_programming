#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10  # Get the last digit and make it positive with abs()
    print("{:d}".format(last_digit), end="")
    return last_digit
