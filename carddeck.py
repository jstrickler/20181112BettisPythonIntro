#!/usr/bin/env python
import random

class CardDeck():
    SUITS = 'Clubs Diamonds Hearts Spades'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self, dealer):
        self.dealer = dealer
        self._create_deck()

    def _create_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards


    def draw(self):
        return self._cards.pop()

    def shuffle(self):
        random.shuffle(self._cards)

    def get_dealer(self):
        return self._dealer

    def set_dealer(self, dealer):
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")


    # getter property
    @property
    def dealer(self):
        return self._dealer

    # setter property
    @dealer.setter
    def dealer(self, dealer):
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    # prop
    @property
    def spam(self):
        return 5

    # props
    @property
    def ham(self):
        return stuff

    @ham.setter
    def ham(self, value):
        pass

    @property
    def alf(self):
        return self._alf

    @alf.setter
    def alf(self, value):
        self._alf = value

    @classmethod
    def get_suits(cls):
        return cls.SUITS

    def __len__(self):
        return len(self._cards)


    def __str__(self):
        my_type = type(self)
        my_type_name = my_type.__name__
        my_len = len(self)
        return "{}({})".format(
            my_type_name, my_len
        )

    def __add__(self, other):
        my_type = type(self)
        # tmp = CardDeck("dealer")
        tmp = my_type(self.dealer)
        tmp._cards = self.cards + other.cards
        return tmp

