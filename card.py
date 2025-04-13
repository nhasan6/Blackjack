class Card:
    # constructor 
    def __init__(self, suit, rank): 
        self._suit = suit # string
        self._rank = rank # string 
        self._face_up = False # boolean 

    def __str__(self):
        if self._face_up:
            return f"{self._rank} of {self._suit}"
        else:
            return "Face Down"
        
    def reveal_card(self):
        self._face_up = True
    
    def hide_card(self):
        self._face_up = False

    def get_suit(self):
        return self._suite

    def get_rank(self):
        return self._rank

    def get_state(self): # Unsure if this is necessary 
        return self._face_up

        # might be good for a count hand function
        # if isinstance(self.rank, int):
        #     self.value = rank # 2 - 19
        # else:
        # use Q, K, J, A no need for words
        # create a function that calculates hand value. 
        #     if self.rank.upper() == "" or self.rank.upper() == "JACK" or self.rank.upper()

class Main:
    test = Card("Spades", 2)
    other_test = Card("Diamonds", "J")
    other_test.reveal_card()
    print(other_test)
    print(test)
            
