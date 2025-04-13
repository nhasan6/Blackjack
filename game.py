from card import Card
from deck import Deck
from player import Player

class Game:
    def __init__(self):
        self._dealer = [] # dealer's hand (represented as a list). * remember that default card values are face down*
        self._players = [] # list of Players
        self._deck = Deck() 
        self._turn = 0

    def start_game(self):
        num_players = int(input("Please enter the number of players (1 - #) who would like to play: "))
        for i in range(1, num_players+1):
            self._players.append(Player(input(f"Player {i}, please enter your name: ")))
        print(f"{num_players} players have been successfully added to the game!")
        print()

    def deal_initial_cards(self):
        # deal first card
        for player in self._players: 
            player.draw_card(self._deck.deal_card())
            print(f"{player.get_name()}'s Hand: {player.get_hand()}")
        
        face_up_card = self._deck.deal_card() # dealer's first card is shown
        face_up_card.reveal_card() 
        self._dealer.append(face_up_card)
        print(f"Dealer's Hand: {self._dealer}")

        # deal second card
        for player in self._players:
            player.draw_card(self._deck.deal_card())
            print(f"{player.get_name()}'s Hand: {player.get_hand()}")
        
        self._dealer.append(self._deck.deal_card()) # dealer's second card is hidden
        print(f"Dealer's Hand: {self._dealer}")

    def check_win_condition:
    

    def player_turn(self):
        print(f"{self._players[self._turn]}'s Turn")




            

        self._turn += 1
    
class Main: 

    blackjack = Game()
    blackjack.start_game()
    blackjack.deal_initial_cards()






