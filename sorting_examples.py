#!/usr/bin/env python

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n1 = sorted(nums)
print('n1:', n1, '\n')

n2 = sorted(nums, reverse=True)
print('n2:', n2, '\n')

fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f0 = sorted(fruits)
print("f0:", f0, '\n')

# str.lower
x = "WOMBAT Rules"
print(str.lower(x))

f1 = sorted(fruits, key=str.lower)
print("f1:", f1, '\n')

def ignore_case(e):
    return e.lower()

ff1 = sorted(fruits, key=ignore_case)

ff2 = sorted(fruits, key=lambda e: e.lower())




f2 = sorted(fruits, key=len)
print("f2:", f2, '\n')

def custom_sort(element):
    return len(element), element.lower()

f3 = sorted(fruits, key=custom_sort)
print("f3:", f3, '\n')

def weird(e):
    return e[-1]

f4 = sorted(fruits, key=weird)
print("f4:", f4, '\n')

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

for first_name, last_name, product in sorted(people):
    print(first_name, last_name)
print('-' * 60)

def by_last_name(person):
    return person[1], person[0]

for first_name, last_name, product in sorted(people, key=by_last_name):
    print(first_name, last_name)
print('-' * 60)

f5 = sorted(fruits, key=lambda e: e.lower())
print("f5:", f5, '\n')

f6 = sorted(fruits, key=lambda e: (len(e), e.lower()))
print("f6:", f6, '\n')

airports = {
    'EWR': 'Newark',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SAC': 'Sacramento',
    'IAD': 'Dulles',
}

for abbr, name in sorted(airports.items()):
    print(abbr, name)
print()

print(airports.items())

for abbr, name in sorted(airports.items(), key=lambda e: (e[1], e[0])):
    print(abbr, name)
print()

fruits.sort(key=str.lower)
print(fruits, '\n')

n3 = sorted(nums, key=str)

print('n3:', n3, '\n')
