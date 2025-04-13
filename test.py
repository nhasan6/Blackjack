from card import Card
from deck import Deck
from player import Player

# test set up

test_deck = Deck()
test_deck.shuffle()

test_player = Player()
test_dealer_hand = []

# game class 

def count_hand(card_hand):
    sum = 0
    ace_counter = 0
    if len(card_hand) > 0: 
        for card in card_hand:
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

def deal_initial_cards():
    test_player.draw_card(test_deck.deal_card())
    test_dealer_hand.append(test_deck.deal_card()) 

    # test_player.draw_card(test_deck.deal_card())
    # hidden_card = test_deck.deal_card()
    # hidden_card.hide_card() # hide dealer's second card
    # test_dealer_hand.append(hidden_card)


# def reset_round():
#     player_hand.reset_hand()
#     cards.reset_deck()
#     #also need to reset the bet
#     #also need to reset the dealer hand

# def player_turn():
#     while player.get_hand().count_hand() < 21: #can either set a variable for player hand, but will constantly need to update that or keep using the getters
#     elif player.get

# place bet 

# deal cards

# player_hand # deal card
# dealer_hand # deal card

# player hand # deal card
# player hand # deal hidden card

# turn

# while card < 21
# display card counter
# option: stay or hit
# if stay:
#     end turn
# if hit:
#     new card-
#     card counter

# test code

deal_initial_cards()
print(test_player.get_hand())
print(count_hand(test_player.get_hand()))
print(test_dealer_hand)
print(count_hand(test_player.get_hand()))












