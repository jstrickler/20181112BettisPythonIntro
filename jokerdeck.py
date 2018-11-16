#!/usr/bin/env python

from carddeck import CardDeck

class JokerDeck(CardDeck):

    def _create_deck(self):
        super()._create_deck()
        for i in range(1,3):
            card = i, 'Joker'
            self._cards.append(card)
