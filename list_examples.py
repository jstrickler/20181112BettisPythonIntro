#!/usr/bin/env python

list1 = list()  # empty list


values = [5.4, 9.8, 2.3]
stuff = ["spam", 12, None, True]  # uncommon

row1 = ['Apple', 'Apricot', 'Artichoke']
row2 = ['Banana', 'Blackberry', 'Bean', 'Borscht']
food = [row1, row2, 'weird!']

print(food, '\n')
print(row1[0])
print(food[0][0])
print(food[0][0][0])
print(row1[len(row1)-1])
print(row2[-2])
print(food[-2][-1][-1], '\n')

cities = ['Pittsburgh', 'Beaver Falls',
         'Confluence', "Homestead", "Boston",
          'McKeesport']

print(cities)
print(cities[0], '\n')
cities.append("Hershey")
print(cities, '\n')
cities.insert(0, 'Philadelphia')
print(cities, '\n')
cities.insert(5, 'Harrisburg')
print(cities, '\n')

more_cities = ['Erie', 'Centralia']

cities.extend(more_cities)

print(cities, '\n')

cities[0] = 'Philly'

print(cities, '\n')

print(len(cities), '\n')

del cities[0] # index or lookup operator
print(cities, '\n')

cities.remove('Confluence')
print(cities, '\n')

x = cities.pop(0)  # function invoker
print(x)
print(cities, '\n')

x = cities.pop()
print(x)
print(cities, '\n')

# city = 'Schartleville'
# del city
# print(city)

cities.extend(['Beaver Falls', 'Rochester',
              'Sewickley'])

print(cities)

print(cities[0], cities[3], cities[-1])

#  SEQUENCE[INDEX]
#  S[START:STOP]  S[:STOP]  S[START:]
#  S[START:STOP:STEP]

print(cities[:3], '\n')
print(cities[6:], '\n')
print(cities[4:8], '\n')
print(cities[:], '\n')

c2 = cities # does NOT create a new list
c2.append('Gettysburg')
print(cities, '\n')

c3 = cities[:]  # DOES create a new list
c3.append('Lancaster')
print(cities, '\n')

c4 = list(cities)

cities[4:8] = ['Exton', 'Greensburg']
print(cities, '\n')

# cities[4:6] = []  # delete > 1

