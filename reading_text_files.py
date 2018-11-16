#!/usr/bin/env python

with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip('\r\n')
        print(line)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    contents = mary_in.read()
    print(len(contents))
    print(contents)
    print()
    print(repr(contents))
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    lines_with_nl = mary_in.readlines()
    print(lines_with_nl)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    lines_without_nl = [line.rstrip() for line in mary_in]
    print(lines_without_nl)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    lines_without_nl_gen = (line.rstrip() for line in mary_in)
    print(lines_without_nl_gen)
    for line in lines_without_nl_gen:
        print(line)
print('-' * 60)


with open('DATA/mary.txt') as mary_in:
    print("round 1")
    for raw_line in mary_in:
        line = raw_line.rstrip('\r\n')
        print(line)
    mary_in.seek(0)   # .seek(0,2) # .seek(-10, 1)
    here = mary_in.tell()
    print("I am at byte", here)
    print("round 2")
    for raw_line in mary_in:
        line = raw_line.rstrip('\r\n')
        print(line)

print('-' * 60)

target_word = 'zombie'

with open('DATA/mary.txt') as mary_in:

    for i, line in enumerate(mary_in, 1):
        line = line.rstrip()
        if target_word in line:
            print("{}: {}".format(i, line))
            break
    else:
        print("not found!")

with open('DATA/mary.txt') as mary_in:
    contents = mary_in.read()
    print(target_word in contents)
    print(contents.find(target_word))



