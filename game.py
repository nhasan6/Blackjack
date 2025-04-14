from card import Card
from deck import Deck
from player import Player, Dealer

class Game:
    def __init__(self):
        self._dealer = Dealer("Dealer") # dealer's hand
        self._players = [] # list of Players
        self._deck = Deck() 
        self._rounds = 0 # number of rounds played
        self._game_active = True # controls the game loop

    def game_loop(self):
        self.start_game()
        while self._game_active:
            self._rounds += 1
            print(f"Round # {self._rounds}")
            self.new_round()
            self.play_round()
            choice = "" == input("Press enter to play another round, anything else to quit: ")
            print() # spacing
            self._game_active = choice
        print("Thanks for playing!")

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
        
        self._dealer.draw_card(self._deck.deal_card()) # dealer's first card is shown
        print(f"Dealer's Hand: {self._dealer.get_hand()}")
        print() # terminal spacing

        # deal second card
        for player in self._players:
            player.draw_card(self._deck.deal_card())
            print(f"{player.get_name()}'s Hand: {player.get_hand()}")
        
        self._dealer.draw_hidden_card(self._deck.deal_card()) # dealer's second card is hidden
        print(f"Dealer's Hand: {self._dealer.get_hand()}")
        print() # terminal spacing to separate the next turn

    def new_round(self): # alt, reset round
        for player in self._players:
            player.reset_hand() 
        self._dealer.reset_hand()
        self._deck.reset_deck() 

    def player_turn(self, player):
        print(f"{player.get_name()}'s Turn")
        turn_active = True
        while player.count_hand() < 21 and turn_active:
            print(f"Current hand value: {player.count_hand()}")
            choice = input("Would you like to (H)it or (S)tay?: ")
            if choice == "S":
                turn_active = False
                break
            elif choice == "H":
                player.draw_card(self._deck.deal_card())
                print(player.get_hand())
            else:
                print("It seems you have chosen an unavailable option. Please try again.")
        print() # terminal spacing btwn the next player's turn

    def dealer_turn(self):
        print("Dealer's Turn")
        self._dealer.get_hand()[1].reveal_card() # reveal dealer's second card
        print(self._dealer.get_hand())
        while self._dealer.count_hand() < 16:
            self._dealer.draw_card(self._deck.deal_card())
            print(self._dealer.get_hand())

    def play_round(self):
        self.deal_initial_cards()
        for player in self._players:
            self.player_turn(player)
        self.dealer_turn()
        for player in self._players:
            self.get_round_result(player, self._dealer)
        
    def get_round_result(self, player, dealer):
        if player.is_blackjack() and dealer.is_blackjack() or player.is_bust() and dealer.is_bust() or player.count_hand() == dealer.count_hand():
            print(f"{player.get_name()}'s result: Tie! (Not counted as a win)")
        elif player.is_blackjack() or dealer.is_bust() or (not player.is_bust() and player.count_hand() > dealer.count_hand()):
            print(f"{player.get_name()}'s result: Win!")
            player.record_win()
        else:
            print(f"{player.get_name()}'s result: Sorry, you lost :(")