#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        read_file = f.read()
    print(read_file)
