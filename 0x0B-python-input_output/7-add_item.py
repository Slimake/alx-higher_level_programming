#!/usr/bin/python3
"""
7-add_item module

Contains save_to_json_file function and load_from_json_file function
adds all arguments to a Python list and save them to a file
"""
from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

i = 1
while i < len(argv):
    my_list.append(argv[i])
    i += 1

save_to_json_file(my_list, filename)
