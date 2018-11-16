#!/usr/bin/env python

person = 'Bill', 'Gates', 'Microsoft'

print(type(person))

print(person[0], person[1])

print(dir(person))
print(person.count('Bill'))

#  list-of-variables = ITERABLE
# person[0]  person[1]  person[2]
first_name, last_name, product = person

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

for first_name, last_name, product in people:
    print(first_name, last_name)
print('-' * 60)

for i, (first_name, last_name, product) in enumerate(people):
    print(i, first_name, last_name)
print('-' * 60)

singleton = 5,
print(singleton)
print(type(singleton))

list_of_tuples_one = [(1, 2), (3, 4)]
print("one:", list_of_tuples_one)

t1 = 1, 2
t2 = 3, 4
list_of_tuples_two = [t1, t2]
print("two:", list_of_tuples_two)

x, y, *z = ['a', 'b', 'c', 'd', 'e', 'f']
print(x, y, z)

x, *y, z = ['a', 'b', 'c', 'd', 'e', 'f']
print(x, y, z)

*x, y, z = ['a', 'b', 'c', 'd', 'e', 'f']
print(x, y, z)





