#!/usr/bin/env python

LIMIT = 1000000

flags = [True] * LIMIT

for i in range(2, LIMIT):
    if flags[i]: # if i is prime...
        print(i, end=", ")
        for j in range(2 * i, LIMIT, i):
            flags[j] = False


