from src.deck import Deck

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
    
    def count_hand(self):
        sum = 0
        ace_counter = 0
        if len(self._hand) > 0: 
            for card in self._hand:
                if card.get_rank().isdigit(): # if rank is from 2 - 9
                    sum += int(card.get_rank()) 
                elif card.get_rank() == "J" or card.get_rank() == "Q" or card.get_rank() == "K": 
                    sum += 10
                else: # Ace
                    ace_counter += 1
                    sum += 11 # sets 11 as the default Ace value

            while ace_counter > 0 and sum > 21: # If the sum exceeds 21, changes Ace values from 11 to 1
                sum -= 10
                ace_counter -=1
            
        return sum # int
    
    def is_blackjack(self):
        return self.count_hand() == 21
    
    def is_bust(self):
        return self.count_hand() > 21
    
    def record_win(self):
        self._wins += 1

class Dealer(Player):
    def __init__(self, name):
        super().__init__(name)

    def draw_hidden_card(self, card):
         if card != None:
            self._hand.append(card) # adds card to hand and sets it to face up








