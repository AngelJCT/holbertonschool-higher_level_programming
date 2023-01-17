#!/usr/bin/python3
def uppercase(str):
    new_str = "" # new string to hold uppercase letters
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122: # if lowercase
            new_str += chr(ord(str[i]) - 32) # convert to uppercase by subtracting 32 from ASCII value and converting back to char
        else:
            new_str += str[i] # if not lowercase, just add to new string
    print("{:s}".format(new_str), end="") # print new string without newline
    print() # print new line
