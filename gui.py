import pygame

# general setup
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
running = True

while running:

    # event loop
    for event in pygame.event.get():

        # exit the game if the user clicks the red "X" 
        if event.type == pygame.QUIT:
            running = False

    # draw the game

    # fills the screen with a background colour
    screen.fill((29,127,124))
    pygame.display.flip()

pygame.quit()