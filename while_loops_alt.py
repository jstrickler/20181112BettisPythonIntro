#!/usr/bin/env python

do_loop = True
while do_loop:
    user_name = input("What is your name (or q to quit)? ")
    if user_name == 'q':
        do_loop = False

    if user_name == '':
        print("** Please enter a name **")

    if not do_loop:
        print("Hello,", user_name)

# not pythonic:
i = 0
while i < 4:
    print(i)
    i += 1
