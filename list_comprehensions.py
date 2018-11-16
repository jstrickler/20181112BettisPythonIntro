#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0", f0, '\n')

f1 = [f.upper() for f in fruits]
print("f1", f1, '\n')

# [EXPR-TO-APPEND for VAR ... in ITERABLE]
# [EXPR-TO-APPEND for VAR ... in ITERABLE if CONDITION ...]

f2 = [f.upper() for f in fruits if f.startswith('p') if len(f) > 5]
print("f2", f2, '\n')

f3 = [f for f in fruits if f.startswith('p') if len(f) > 5]
print("f3", f3, '\n')

f4 = [f for f in fruits if not f.startswith('p')]
print("f4", f4, '\n')

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n1 = [float(n) + 5 for n in nums if n > 300]
print("n1:", n1, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux'),
]

last_names = [p[1] for p in people]
print(last_names, '\n')

last_names_gen = (p[1] for p in people)
print(last_names_gen)
for last_name in last_names_gen:
    print(last_name)






