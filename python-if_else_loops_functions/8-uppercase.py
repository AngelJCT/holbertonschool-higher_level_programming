#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            new_str += chr(ord(str[i]) - 32)
        else:
            new_str += str[i]
    print("{:s}".format(new_str), end="")
    print()
