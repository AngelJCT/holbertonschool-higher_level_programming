#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:  # if i is divisible by 3 and 5
            print("FizzBuzz", end="")
        elif i % 3 == 0:  # if i is divisible by 3
            print("Fizz", end="")
        elif i % 5 == 0:  # if i is divisible by 5
            print("Buzz", end="")
        else: # if i is not divisible by 3 or 5
            print("{:d}".format(i), end="")  # print i
        print(" ", end="")  # print a space
