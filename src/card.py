class Card:
    # constructor 
    def __init__(self, suit, rank): 
        self._suit = suit # string
        self._rank = rank # string 
        self._face_up = False # boolean 

    def __str__(self):
        if self._face_up:
            return f"{self._rank}{self._suit}" # temporary string display
        else:
            return "Face Down"
        
    def __repr__(self):
        return self.__str__() # calls the to-string function if a list of card objects are printed
    
    def reveal_card(self):
        self._face_up = True
    
    def hide_card(self):
        self._face_up = False

    def get_suit(self):
        return self._suit

    def get_rank(self):
        return self._rank

    def get_state(self): # Unsure if this is necessary 
        return self._face_up