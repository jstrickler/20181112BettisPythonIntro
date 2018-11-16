#!/usr/bin/env python

# == != > < >= <= is

x = 10
y = 11

print(x == y, x != y)
print(x > y, x < y)
print(x <= y, x >= y)
print(x is y)

spam = None

if spam is None:
    print("Whoa!")


#  and  or  not

print(12 and 5)
print(0 and 5)
print("" and 5)
print(12 and 0)

print(12 or 7)
print(0 or 7)

print(not 0, not 7, not 8, not None, not '')

print()

#  & | ^

print(12 | 4, bin(12), bin(4))
print(12 ^ 4, bin(12), bin(4))
print(5 & 6, bin(5), bin(6))

x = 5
print(type(x))

x = 5
x = "wombat"
x = 1.2
x = True
x = None









