#!/usr/bin/env python

a = 'apple'
b = 234
c = 23.239029
d = 239030920392093

print(a, b, c)
print(a, b, c, sep='_')
print(a, b, c, sep=' == ')
print(a, b, c, sep='')

print(a, b, end="...")
print(c)

#       0                  1         0  1
print("{} is selling for ${}".format(a, b))

#  "...{}...{}....".format(p1, p2)

print("{0} {0} {0}".format(a))

print("c is {}".format(c))
print("c is {:.2f}".format(c))
print("{:,d}".format(d))

first_name = 'Barney'
last_name = 'Rubble'

width = 12
print("|{0:>{3}s}|{1:{3}s}|{2:^{3}s}|".format(first_name, last_name, last_name, width))



