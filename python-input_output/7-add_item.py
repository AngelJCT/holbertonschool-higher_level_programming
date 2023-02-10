#!/usr/bin/python3
"""Module 7-add_item"""


import sys
from os import path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if not path.exists("add_item.json"):
    items = []
else:
    items = load_from_json_file("add_item.json")

for i in range(1, len(sys.argv)):
    items.append(sys.argv[i])

save_to_json_file(items, "add_item.json")
