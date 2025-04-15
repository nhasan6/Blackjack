from card import Card
from deck import Deck
from player import Player, Dealer
from game import Game

def main():
    blackjack = Game()
    blackjack.game_loop()

if __name__ == "__main__":
    main()
    