#!/usr/bin/env python

while True:
    user_name = input("What is your name (or q to quit)? ")
    if user_name == 'q':
        break
    elif user_name == '':
        print("** Please enter a name **")
        continue
    else:
        print("Hello,", user_name)

# not pythonic:
i = 0
while i < 4:
    print(i)
    i += 1
