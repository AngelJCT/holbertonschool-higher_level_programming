#!/usr/bin/python3
def multiple_returns(sentence):
    new_tuple = (len(sentence), sentence[0])
    if new_tuple[0] == 0:
        sentence[0] = None
    return new_tuple
