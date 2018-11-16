#!/usr/bin/env python

cave_man = 'Barney Rubble'

print(len(cave_man))

print(cave_man.upper())

#  func()
#  func(arg1, arg2, ...)
print(cave_man)
print(cave_man.count('b'))
print(cave_man.lower().count('b'))
print(cave_man.casefold().count('b'))
print(cave_man.startswith('A'))
print(cave_man.startswith('B'))
print(cave_man.endswith('e'))
print(cave_man.endswith('f'))
print(cave_man.find('Rub'))
print(cave_man.index('Rub'))
print(cave_man.find('Fred'))
a = "1234"
b = "-12.3"
print(a.isdigit())
print(b.isdigit())
print(a.isnumeric())
print(b.isnumeric())

s1 = "    All my exes live in Texas    "
print("|" + s1.lstrip() + "|")
print("|" + s1.rstrip() + "|")
print("|" + s1.strip() + "|")
print()

s2 = "xxxyyyxyxxxxyyyyAll my exes live in Texasxyyxxyyxxyyxxyyyyy"
print("|" + s2.lstrip('xy') + "|")
print("|" + s2.rstrip('xy') + "|")
print("|" + s2.strip('xy') + "|")
print()

s3 = "All my exes live in Texas"
print(s3.replace(' ', '_'), '\n')
print(s3.replace('Texas', 'Connecticut'))

name_str = 'Fred    Barney     Wilma    Betty'
names = name_str.split()
print(names)

mac_address = "AB:CD:EF:12:FE:DC"
octets = mac_address.split(':')
print(octets)
