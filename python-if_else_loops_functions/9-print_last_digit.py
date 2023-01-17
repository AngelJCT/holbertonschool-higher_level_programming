#!/usr/bin/python3
def print_last_digit(number):
    last_digit = number
    if last_digit < 0:  # if negative
        last_digit = number * -1
    else:  # if positive
        last_digit = number % 10  # get last digit
    print("{:d}".format(last_digit), end="")  # print last digit
    return last_digit  # return last digit
