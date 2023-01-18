#!/usr/bin/python3
counter = 0  # initialize counter
alphabet = "" # initialize alphabet

for i in range(ord('z'), ord('a') - 1, - 1):  # ord() returns the ASCII value of the character
    c = chr(i)  # chr() returns the character of the ASCII value
    if counter % 2 == 0: # if counter is even
        alphabet = "{}".format(c.lower())  # lower() returns the lowercase version of the string
    else:  # if counter is odd
        alphabet = "{}".format(c.upper())  # upper() returns the uppercase version of the string
    counter += 1  # increment counter
    print(alphabet, end="")  # print alphabet without a new line
