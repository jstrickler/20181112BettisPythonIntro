#!/usr/bin/env python
"""
Read data about Monty Python's knights

"""
from pprint import pprint

MAX_TRIES = 18

def main():
    """
    Program entry point

    :return: None
    """
    d = read_data()
    pretty_print(d)
    print_titles(d)


def read_data():
    """
    Read data from colon-delimited file.

    :return: Dictionary, indexed by name
    """
    data = {}

    with open('DATA/knights.txt') as knights_in:

        for raw_line in knights_in:
            line = raw_line.rstrip()
            name, title, color, quest, *comment = line.split(':')
            data[name] = title, color, quest, comment
    return data

def pretty_print(knight_data):
    pprint(knight_data)
    print()

def print_titles(knight_data):
    for knight_name, knight_info in knight_data.items():
        print(knight_info[0], knight_name)
    print()


if __name__ == '__main__':
    main()
