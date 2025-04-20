import pygame
from button import Button
from src.card import Card
from src.deck import Deck
from src.player import Player, Dealer
from src.game import Game 

def illustrate_card(card, x, y):
    card_surf = pygame.Surface((150,200)) # size of cards
    card_surf.fill("white")
    card_rect = card_surf.get_frect(midtop = (x, y)) 
    screen.blit(card_surf, card_rect)
    if card.get_state():
        text_surf = game_font.render(f"{card.get_rank()} of {card.get_suit()}", True, "Black")
        text_rect = text_surf.get_frect(center = ((x - 10,y+40))) # put text slightly below the top
        screen.blit(text_surf, text_rect) 
    else:
        text_surf = game_font.render(f"Hidden", True, "Black")
        text_rect = text_surf.get_frect(center = ((x - 10,y+40))) # put text slightly below the top
        screen.blit(text_surf, text_rect) 


def illustrate_hand(player, x, y):
        for card in player.get_hand():
            illustrate_card(card, x, y)
            x += 120 # horizontally stagger the cards

def get_round_result(player):
        if player.is_blackjack() and blackjack.get_dealer().is_blackjack() or player.is_bust() and blackjack.get_dealer().is_bust() or player.count_hand() == blackjack.get_dealer().count_hand():
            return game_font.render("TIE", True, "Black")
        elif player.is_blackjack() or blackjack.get_dealer().is_bust() or (not player.is_bust() and player.count_hand() > blackjack.get_dealer().count_hand()):
            player.record_win()
            return game_font.render("WIN", True, "Black")
        else:
            return game_font.render("LOSE", True, "Black")

# general setup
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Blackjack")
game_font = pygame.font.Font(None, 20)
title_font = pygame.font.Font("./assets/titlefont.ttf", 180)
running = True # pygame main loop (kills the game when false)
game_active = False # whether a game is currently being played
cards_dealt = False
round_active = True
turn_tracker = 0
rounds = 0

# Intialize Game Assets
blackjack = Game()
blackjack.start_game()

# Create buttons
hit_bttn = Button("Hit",(179,133,182), "black", (250, SCREEN_HEIGHT * 3/4))
stay_bttn = Button("Stay",(179,133,182), "black", (SCREEN_WIDTH - 250, SCREEN_HEIGHT * 3/4))

# Dealer and player card "placemats"
dealer_mat = pygame.Surface((175,250))
dealer_mat.fill((248,112,90))
dealer_mat_rect = dealer_mat.get_frect(midtop = (SCREEN_WIDTH/2, 30))
dealer_mat_label = game_font.render("Dealer", True, "Black")
dealer_mat_label_rect = dealer_mat_label.get_frect(midtop = (SCREEN_WIDTH/2, 40))

player_mat = pygame.Surface((175,250))
player_mat.fill((207,118,74))
player_mat_rect = player_mat.get_frect(midtop = (SCREEN_WIDTH/2, 440))
player_mat_label = game_font.render("Player1", True, "Black")
player_mat_label_rect = player_mat_label.get_frect(midtop = (SCREEN_WIDTH/2, 450))

while running:

    # event loop
    for event in pygame.event.get():

        # exit the game if the user clicks the red "X" 
        if event.type == pygame.QUIT:
            running = False
        
        # while a game is currently active/being played
        elif game_active:

            if round_active:
                if turn_tracker < len(blackjack.get_players()):
                    if blackjack.get_players()[turn_tracker].count_hand() < 21:
                        if hit_bttn.check_click():
                            blackjack.get_players()[turn_tracker].draw_card(blackjack.get_deck().deal_card())
                        if stay_bttn.check_click():
                            turn_tracker += 1
                    else:
                        turn_tracker +=1
                
                else:
                    blackjack.dealer_turn()
                    for player in blackjack.get_players():
                        result_surf = get_round_result(player)
                        result_rect = result_surf.get_frect(center = (SCREEN_WIDTH/2, 470))
                        round_active = False

        else:
            # Pygame window is active, but a game is over. If a player wants to continue to thge next round, press space. # this actually doesn't work!!!!
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                blackjack.new_round()
                cards_dealt = False
                turn_tracker = 0
                round_active = True
                
                # this is where any reset round things occur 

    # draw the game

    if not game_active:
        if rounds > 0:
            pass
        else:
            screen.fill((29,127,124))
            title = title_font.render("BLACKJACK", True, "black")
            title_rect = title.get_frect(center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
            screen.blit(title, title_rect)
    else:
        # fills the screen with a background colour
        screen.fill((29,127,124))

        # Draws mat surfaces
        screen.blit(dealer_mat, dealer_mat_rect)
        screen.blit(dealer_mat_label, dealer_mat_label_rect)

        screen.blit(player_mat, player_mat_rect)
        screen.blit(player_mat_label, player_mat_label_rect)

        if not cards_dealt:
            blackjack.deal_initial_cards()
            cards_dealt = True
            rounds += 1

        # Buttons 
        hit_bttn.draw(screen)
        stay_bttn.draw(screen)

        # Display each players hand every time 
        illustrate_hand(blackjack.get_dealer(), SCREEN_WIDTH/2, 60)

        for player in blackjack.get_players():
                illustrate_hand(player, SCREEN_WIDTH/2, 470)

        if not round_active:
            screen.blit(result_surf, result_rect)

    pygame.display.flip()

pygame.quit()