from deck import Deck

class Player:

    # constructor 
    def __init__(self, name):
        self._hand = []
        self._name = name # string 
        self._wins = 0 # num wins
        # self._bet = 

    def draw_card(self, card):
        if card != None:
            card.reveal_card()
            self._hand.append(card) # adds card to hand and sets it to face up
    
    def get_hand(self):
        return self._hand
    
    def reset_hand(self):
        self._hand.clear()

    def get_name(self):
        return self._name
    

    

    

    








