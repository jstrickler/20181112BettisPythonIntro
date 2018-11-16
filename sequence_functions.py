#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

print(len(fruits), len(nums))
print(min(fruits), min(nums))
print(max(fruits), max(nums))
print(sum(nums))
print(sorted(fruits))
print(sorted(nums))

print(list(reversed(nums)))
print(reversed(nums))

#  foo.bar()   # bar() method (AKA function) of foo object
#  spam(foo)   # pass foo object to function spam()
#  del foo     # builtin keyword affects foo

# foo.sort()  # sorts in place (only for lists)
# sorted(foo)  # create new sorted list (ANY iterable)

nums.reverse()
print(nums)
r = reversed(nums)
for num in r:
    print(num)

colors = ['red', 'purple', 'taupe', 'orange']
numbers = [5, 2, 14, 9]

z = zip(colors, numbers)
print(z)
colors[0] = 'pink'
colors.append('blue')
numbers.append(3)
print(list(z))
print('-' * 60)
for index, fruit in enumerate(fruits):
    print(index, fruit)
print('-' * 60)
for index, fruit in enumerate(fruits, 1):
    print(index, fruit)

print('-+' * 30)
flags = [True] * 10
print(flags)
print([1,2,3] * 5)

m = ['a', 'b', 'c'] + ['d', 'e', 'f']
print(m)

print('apple' in fruits)
print('durian' in fruits)

actor = 'Tom Hanks'
print('Han' in actor)
print('Luke' in actor, '\n')

# i = 0
# while i < 10:
#     print(i)
#     i += 1

# range(STOP) range(START, STOP)  range(START, STOP, STEP)
for i in range(1, 11):
    print(i)
print()






















