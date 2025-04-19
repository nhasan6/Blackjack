import pygame

# general setup
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Blackjack")
game_font = pygame.font.Font(None, 20)
title_font = pygame.font.Font("./assets/titlefont.ttf", 40)
running = True


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
player_mat_label_rect = dealer_mat_label.get_frect(midtop = (SCREEN_WIDTH/2, 450))

# Buttons --> there should probably be a way to turn this into a class/obj

hit_bttn = pygame.Surface((175, 80))
hit_bttn.fill((179,133,182))
hit_bttn_rect = hit_bttn.get_frect(center = (250, SCREEN_HEIGHT * 2/3))

stay_bttn = pygame.Surface((175, 80))
stay_bttn.fill((179,133,182))
stay_bttn_rect = hit_bttn.get_frect(midright = (SCREEN_WIDTH-250, SCREEN_HEIGHT * 2/3))

# Fonts
stay_bttn_label = game_font.render("Stay", True, "black")
stay_bttn_label_rect = stay_bttn_label.get_rect(center = stay_bttn_rect.center)

hit_bttn_label = game_font.render("Hit", True, "black")
hit_bttn_label_rect = stay_bttn_label.get_rect(center = hit_bttn_rect.center)


while running:

    # event loop
    for event in pygame.event.get():

        # exit the game if the user clicks the red "X" 
        if event.type == pygame.QUIT:
            running = False


    # draw the game

    # fills the screen with a background colour
    screen.fill((29,127,124))


    # test blits for buttons/surfaces
    screen.blit(dealer_mat, dealer_mat_rect)
    screen.blit(dealer_mat_label, dealer_mat_label_rect)

    screen.blit(player_mat, player_mat_rect)
    screen.blit(player_mat_label, player_mat_label_rect)


    screen.blit(hit_bttn, hit_bttn_rect)
    screen.blit(hit_bttn_label, hit_bttn_label_rect)


    screen.blit(stay_bttn, stay_bttn_rect)
    screen.blit(stay_bttn_label, stay_bttn_label_rect)



                                                                                                                                                                                                                                               

    pygame.display.flip()

pygame.quit()