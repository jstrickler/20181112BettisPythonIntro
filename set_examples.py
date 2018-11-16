#!/usr/bin/env python

john_countries = """Canada
Mexico
Barbados
China
UK
Austria
Spain
Bulgaria
Israel""".split()

clare_countries = """Denmark
UK
Spain
Kenya
Mexico
Barbados
Norway
Sweden
Canada""".split()

clare = set(clare_countries)
john = set(john_countries)

print(clare)
print(john)
print()


print("both:", clare & john, '\n')
print("only one:", clare ^ john, '\n')
print("either:", clare | john, '\n')
print("just Clare:", clare - john)
print("just John:", john - clare)

food = ['spam', 'spam', 'fried chicken', 'spam', 'spam', 'spam', 'eggs']
print(set(food))
print(list(set(food)))


d1 = {'a':5, 'b':6, 'c': 7}
d2 = {'a':3, 'm':9, 'b': 10, 'h': 18}

print(d1.keys() & d2.keys())
print(d1.keys() | d2.keys())
print(d1.keys() - d2.keys())
print(d2.keys() - d1.keys())

k = d1.keys()
# print(isinstance(k, set))  NOT
