#!/usr/bin/python3
""" adds all arguments to a Python list, and then save them to a file """
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    args = load_from_json_file(filename)
except Exception:
    args = []

for i in range(1, len(argv)):
    args.append(argv[i])
save_to_json_file(args, filename)
