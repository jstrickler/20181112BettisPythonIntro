#!/usr/bin/env python
from pprint import pprint

d1 = dict()
d2 = {'red': 5, 'purple': 3, 'blue': 9}
d3 = {}
d4 = dict(red=5, purple=3, blue=9)

pairs = [('red', 5), ('purple', 3),
         ('blue', 9)]
d5 = dict(pairs)

keys = 'red purple blue'.split()
values = 5, 3, 9

d6 = dict(zip(keys, values))

airports = {
    'EWR': 'Newark',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'PIT': 'Pittsburgh',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SAC': 'Sacramento',
    'IAD': 'Dulles',
}

print(airports['PIT'])
airports['PHL'] = 'Philadelphia'
pprint(airports)
print()

airports['PHL'] = 'Philadelphia International Airport'

pprint(airports)
print()

print('PHL' in airports)
print('ELM' in airports)

print(airports.get('ELM'))
print(airports.get('ELM', "NOT FOUND"))
print()

for abbr in 'ELM RDU PIT PHL LAX YYK'.split():
    print(abbr, airports.get(abbr, 'NO SUCH ABBR'))
print()

for abbr in 'ELM RDU PIT PHL LAX YYK'.split():
    print(abbr, airports.setdefault(abbr, 'UNKNOWN'))
print()

pprint(airports)
print()

print(airports.keys())
print(airports.values())
print()

more_airports = {'PDX': 'Portland', 'SEA': 'Seattle', 'IAD': 'Dulles International Airport'}

airports.update(more_airports)
pprint(airports)
print()

things = ['a', 'b', 'c']
print(list(enumerate(things)), '\n')

print(airports.items(), '\n')

for abbr, name in airports.items():
    print(abbr, name)
print()

for abbr, name in sorted(airports.items()):
    print(abbr, name)
print()

# for abbr in sorted(airports):
#     print(abbr, airports[abbr])

