#!/usr/bin/python3
""" load, add, save """
import sys
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

fp = "add_item.json"
ls = load_from_json_file(fp) if os.path.exists(fp) else []

for i in range(1, len(sys.argv)):
    ls.append(sys.argv[i])
save_to_json_file(ls, fp)
