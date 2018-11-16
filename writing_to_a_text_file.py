#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('fruitlist.txt', 'w') as fruitlist_out:
    for fruit in fruits:
        fruitlist_out.write(fruit + '\n')


with open('shortfruits.txt', 'w') as short_out:
    with open('longfruits.txt', 'w') as long_out:
        for fruit in fruits:
            record = fruit + '\n'
            if len(fruit) > 6:
                long_out.write(record)
            else:
                short_out.write(record)


