#!/usr/bin/env python
from pprint import pprint

knight_data = {}

with open('DATA/knights.txt') as knights_in:

    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, *comment = line.split(':')
        knight_data[name] = {
            'title': title,
            'color': color,
            'quest': quest,
            'comment': comment,
        }

pprint(knight_data)
print()

for knight_name, knight_info in knight_data.items():
    print(knight_info['title'], knight_name, knight_info['comment'])
print()

