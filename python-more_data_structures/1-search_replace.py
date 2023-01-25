#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    lambda_func = lambda x: replace if x==search else x
    new_list = list(map(lambda_func, my_list))
    return new_list
