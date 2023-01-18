#!/usr/bin/python3
"""Reading file"""


def read_file(filename=""):
    """Defining function"""
    if filename:
        with open(filename, moder='r', encoding="utf-8") as f:
            for i in f:
                print(i, end="")
