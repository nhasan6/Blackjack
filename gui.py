import pygame
from button import Button
from src.card import Card
from src.deck import Deck
from src.player import Player, Dealer
from src.game import Game
            
# general setup
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Blackjack")
game_font = pygame.font.Font(None, 20)
title_font = pygame.font.Font("./assets/titlefont.ttf", 40)
running = True

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

    # draw the game

    # fills the screen with a background colour
    screen.fill((29,127,124))

    # Draws mat surfaces
    screen.blit(dealer_mat, dealer_mat_rect)
    screen.blit(dealer_mat_label, dealer_mat_label_rect)

    screen.blit(player_mat, player_mat_rect)
    screen.blit(player_mat_label, player_mat_label_rect)

    # Buttons 
    hit_bttn.draw(screen)
    stay_bttn.draw(screen)

    pygame.display.flip()

pygame.quit()