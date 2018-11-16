#!/usr/bin/env python
import sys

# def print(*args):
#     sys.stdout.write('HA HA HA\n')

x = 100  # GLOBAL variable

def spam():
    # x = 42
    print("In spam(): x is", x)
    actor = 'Cary Grant'  # LOCAL variable


spam()
print("in main: x is", x)

