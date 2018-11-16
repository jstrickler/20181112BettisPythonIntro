#!/usr/bin/env python
from copy import deepcopy

row1 = ['Apple', 'Apricot', 'Artichoke']
row2 = ['Banana', 'Blackberry', 'Bean', 'Borscht']
food = [row1, row2]

a = food
b = list(food)
b[0].append('Ambergris')
print(food)

c = deepcopy(food)
c[0].append('Ambrosia')
print(food)
