#!/usr/bin/python3
"""This module contains a file"""
import json
from sys import argv
save_to_file = __import__("5-save_to_json_file").save_to_json_file
load_from_file = __import__("6-load_from_json_file").load_from_json_file


def main():
    """Main function"""
    filename = "add_item.json"
    try:
        arguments = load_from_file(filename)
    except Exception as e:
        arguments = list()
    for i in range(1, len(argv)):
        arguments.append(argv[i])
    save_to_file(arguments, filename)


if __name__ == "__main__":
    main()
