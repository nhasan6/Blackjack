from src.card import Card
from src.deck import Deck
from src.player import Player, Dealer
from src.game import Game

def main():
    blackjack = Game()
    blackjack.game_loop()

if __name__ == "__main__":
    main()
    