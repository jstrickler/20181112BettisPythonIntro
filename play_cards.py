#!/usr/bin/env python
from carddeck import CardDeck
from jokerdeck import JokerDeck

x = 1, 2, 3
list1 = list(x)

d1 = CardDeck("Marsha")

print(d1)

# x = AbaqusFile('floofy.txt')

print(d1._dealer) # BAD

# use getter function
print(d1.get_dealer())

# getter property
print(d1.dealer)

d1.dealer = 'Fred'

print(d1.dealer)

try:
    d2 = CardDeck(1.2)
except TypeError as err:
    print(err)
else:
    print(d2)

d3 = CardDeck("Susan")
d1.shuffle()
print(d1.cards)

hand = []
for i in range(5):
    card = d1.draw()
    hand.append(card)

print(hand)
print(d1.get_suits())
print(CardDeck.get_suits())
print('-' * 60)
j1 = JokerDeck('Laura')
print(j1.dealer)
j1.shuffle()
print(j1.cards)

print(len(d1))
print(d1)
print(j1)

x = d1 + j1
print(x)
y = j1 + d1
print(y)


