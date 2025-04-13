from card import Card
import random

class Deck:
    _SUITS = ["SPADES", "HEARTS","DIAMONDS", "CLUBS"]
    _RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    # constructor
    def __init__(self):
        self._cards = []
        self.reset_deck(self)
    
    def __str__(self):
        return f"{self._cards}"
    
    def shuffle(self):
        random.shuffle(self._cards)

    def reset_deck(self):
        if len(self._cards) > 0:
            self._cards.clear()
        for suit in Deck._SUITS:
            for rank in Deck._RANKS:
                self._cards.append(Card(suit,rank))

class Main:
    practice = Deck()
    practice.shuffle()
    print(practice)


#probably need an out of bounds counter somewhere
        
