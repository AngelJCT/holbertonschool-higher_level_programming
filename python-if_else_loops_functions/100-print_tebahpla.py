#!/usr/bin/python3
counter = 0
alphabet = ""

for i in range(ord('z'), ord('a') - 1, - 1):
    c = chr(i)
    if counter % 2 == 0:
        alphabet = "{}".format(c.lower())
    else:
        alphabet = "{}".format(c.upper())
    counter += 1
    print(alphabet, end="")
