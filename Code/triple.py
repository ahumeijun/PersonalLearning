#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import random

class Card(object):
    suits = ['Club', 'Spade', 'Diamond', 'Heart']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    def __init__(self, value, tag):
        super(Card, self).__init__()
        self.value = value
        self.tag = tag
        self.suit = self.suits[tag - 1]
        self.rank = self.ranks[value -1]

    def __str__(self):
        return '[%s of %s]'%(self.rank, self.suit)

    def __repr__(self):
        return '[%s of %s]'%(self.rank, self.suit)

    def __lt__(self, other):
        if self.value == other.value:
            return self.tag < other.tag
        else:
            return self.value < other.value 
class TripleLevel(object):
    leopard = 0
    sequenceSuits = 1
    suits = 2
    sequence = 3
    pair = 4
    single = 5
        

class Triple(object):
    def __init__(self, card1, card2, card3):
        super(Triple, self).__init__()
        self.cards = []
        self.cards.append(card1)
        self.cards.append(card2)
        self.cards.append(card3)
        self.cards.sort()
        self.level = 0
        self.score = 0
        self.grade()

    def grade(self):
        if self.isSameRank():
            self.level = TripleLevel.leopard
            self.score = self.cards[0].value
        elif self.isSameSuit() and self.isSequence():
            self.level = TripleLevel.sequenceSuits
            self.score = self.cards[2].value * 100 + self.cardsp[2].tag
        elif self.isSameSuit():
            self.level = TripleLevel.suits
            self.score = self.cards[2].value * 1000000 + self.cards[1].value * 10000 + self.cards[0].value * 100 + self.cards[2].tag
        elif self.isSequence():
            self.level = TripleLevel.sequence
            self.score = self.cards[2].value * 100 + self.cards[2].tag
        elif self.isPair():
            self.level = TripleLevel.pair
            singleindex = 0
            pairindex = 2
            if self.cards[0].rank == self.cards[1].rank:
                singleindex = 2
                pairindex = 0
            extra = max(self.cards[1].tag, self.cards[pairindex].tag)
            self.score = self.cards[1].value * 10000 + self.cards[singleindex].value * 100 + extra
        else:
            self.level = TripleLevel.single
            self.score = self.cards[2].value * 1000000 + self.cards[1].value * 10000 + self.cards[0].value * 100 + self.cards[2].tag

    def isSameSuit(self):
        return self.cards[0].suit == self.cards[1].suit and self.cards[1].suit == self.cards[2].suit
    
    def isSameRank(self):
        return self.cards[0].rank == self.cards[1].rank and self.cards[1].rank == self.cards[2].rank
    
    def isSequence(self):
        return self.cards[2].value - self.cards[1].value == 1 and self.cards[1].value - self.cards[0].value == 1

    def isPair(self):
        return self.cards[0].rank == self.cards[1].rank or self.cards[1].rank == self.cards[2].rank

    def __lt__(self, other):
        if self.level == other.level:
            return self.score < other.score
        else:
            return self.level > other.level

class Deck(object):
    def __init__(self, count):
        super(Deck, self).__init__()
        self.deap = []
        for i in range(0, count):
            for v in range(1, 14):
                for t in range(1, 5):
                    card = Card(v, t)
                    self.deap.append(card)
        self.cards = self.deap[:]
        self.triples = self.combination()
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deap)
        self.cards = self.deap[:]

    def combination(self):
        triples = []
        temp = self.cards[:]



if __name__ == '__main__':
    deck = Deck(1)
    print(deck.cards)
    triple = Triple(deck.cards[0], deck.cards[1], deck.cards[2])
    print(triple.cards)
    print(triple.level)
    print(triple.score)

