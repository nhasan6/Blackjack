from card import Card
import random

class Deck:
    _SUITS = ["SPADES", "HEARTS","DIAMONDS", "CLUBS"]
    _RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] 

    # constructor
    def __init__(self):
        self._cards = []
        self.reset_deck()
    
    def __str__(self):
        return f"{self._cards}"
    
    def shuffle(self):
        random.shuffle(self._cards)

    def reset_deck(self):
        if len(self._cards) > 0: # checks if there are still cards left over from the last round
            self._cards.clear()
        for suit in Deck._SUITS: # repopulates the deck 
            for rank in Deck._RANKS:
                self._cards.append(Card(suit,rank))
    
    def deal_card(self):
        if len(self._cards) > 0: # checks if the deck still has cards 
            card = self._cards[0] # chooses the first card in the deck
            self._cards.pop(0) # removes the card from the deck
            return card # returns the card obj, which can then be drawn by a player/the dealer
        else:
            print("There are no cards left in the deck")
            return None 

#probably need an out of bounds counter somewhere
        
