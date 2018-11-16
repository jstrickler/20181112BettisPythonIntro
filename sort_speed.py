#!/usr/bin/env python
import timeit

setup_code = """
fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

def ignore_case(e):
    return e.lower()
"""

codes = [
    '''f = sorted(fruits, key=str.lower)''',
    '''f = sorted(fruits, key=ignore_case)''',
    '''f = sorted(fruits, key=lambda e: e.lower())''',
]

for code in codes:
    t = timeit.Timer(code, setup_code)
    print(code, '\n')
    print(t.timeit(10000))
    print()

