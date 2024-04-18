#!/usr/bin/python3
"""Module 7-add_item.py
"""
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"
len_argv = len(sys.argv)

try:
    py_obj = load_from_json_file(filename)
except Exception:
    py_obj = []

if len_argv != 1:
    for arg in sys.argv[1:]:
        py_obj.append(arg)

save_to_json_file(py_obj, filename)
