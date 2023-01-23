#!/usr/bin/python3
def multiple_returns(sentence):
    new_tuple = ()
    if len(sentence) == 0:
        sentence[0] = None
    else:
        new_tuple = (len(sentence), sentence[0])
        return new_tuple
