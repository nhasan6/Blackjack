import os

import pygame
from src.button import Button
from src.card import Card
from src.deck import Deck
from src.player import Player, Dealer

BASE_DIR = os.path.dirname(__file__)

def deal_initial_cards(players, dealer, deck):    
   # deal first card
   for player in players:
       player.draw_card(deck.deal_card())
   dealer.draw_card(deck.deal_card()) # dealer's first card is shown


   # deal second card
   for player in players:
       player.draw_card(deck.deal_card())
   dealer.draw_hidden_card(deck.deal_card()) # dealer's second card is hidden


def reset_round(players, dealer, deck, results):
   for player in players:
       player.reset_hand() # clears each player's hand
   dealer.reset_hand()
   deck.reset_deck()  # replenishes and shuffles the deck
   results.clear() # clears the rounds results


def dealer_turn():
   dealer.get_hand()[1].reveal_card() # reveal dealer's second card
   while dealer.count_hand() < 16 and deck.get_length() > 0: # dealer must keep drawing cards until their total is >=16 and there are still cards left in the draw pile
       dealer.draw_card(deck.deal_card())


def illustrate_card(card, x, y):
   # displays a playing card on the screen
   if card.get_state(): # if card is revealed
       card_surf = pygame.image.load(os.path.join(BASE_DIR, "assets", f"img/{card.get_rank()}{card.get_suit()}.png")).convert_alpha()
   else: # if card is hidden
       card_surf = pygame.image.load(os.path.join(BASE_DIR, "assets", "img/back.png")).convert_alpha()
   card_surf = pygame.transform.scale(card_surf, (150,200)) # resize cards
   card_rect = card_surf.get_frect(topleft = (x, y))
   screen.blit(card_surf, card_rect)


def illustrate_hand(player, x, y):
   # displays all the cards in a player/dealer's hand on the screen
   for card in player.get_hand():
       illustrate_card(card, x, y)
       x += 30 # spaces out the cards horizontally


def illustrate_total(player, x, y):
   # displays the total value of a hand of cards on the screen
   total_surf = REG_FONT.render(f"{player.count_hand()}", True, "Black")
   total_rect = total_surf.get_frect(midleft = (x,y))
   screen.blit(total_surf, total_rect)


def illustrate_wins(player, x,y):
   # displays the a players win count on the screen
   wins_surf = REG_FONT.render(f"Wins: {player.get_wins()}", True, "Black")
   wins_rect = wins_surf.get_frect(midtop = (x,y))
   screen.blit(wins_surf, wins_rect)


def get_round_result(player):
   # determines the outcome of the round for an individual player and returns a text surface with the outcome
   if (player.is_blackjack() and dealer.is_blackjack()) or (player.is_bust() and dealer.is_bust()) or (player.count_hand() == dealer.count_hand()):
       return RESULT_FONT.render("TIE", True, "Black")
   elif (player.is_blackjack() or dealer.is_bust()) or ((not player.is_bust() and (player.count_hand() > dealer.count_hand()))):
       player.record_win()
       return RESULT_FONT.render("WIN", True, "Black")
   else:
       return RESULT_FONT.render("LOSE", True, "Black")
      
def enroll_players():
   num_players = int(input("Please enter the number of players (1-3): "))
   for i in range(1, num_players+1):
       players.append(Player(f"Player {i}"))


# general pygame setup
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Blackjack")
clock = pygame.time.Clock()


# load fonts
REG_FONT = pygame.font.Font(None, 20)
FONT_PATH = os.path.join(BASE_DIR, "assets", "titlefont.ttf")
TITLE_FONT = pygame.font.Font(FONT_PATH, 180)
RESULT_FONT = pygame.font.Font(FONT_PATH, 70)


# intialize blackjack objects
dealer = Dealer("Dealer") # dealer's hand
players = [] # list of players
deck = Deck()
results = [] # list of tuples with result surfaces and rects, to be displayed on the screen at the end of each round


# game-control variables
running = True # controls main pygame loop (kills the screen when false)
game_active = False # controls whether a game/round is currently being played
turn_tracker = 0 # tracks which players turn it is
rounds = 0 # number of rounds played
cards_dealt = False
players_enrolled = False


# Create buttons
hit_bttn = Button("Hit",(179,133,182), "black", (250, SCREEN_HEIGHT * 1/3))
stay_bttn = Button("Stay",(179,133,182), "black", (SCREEN_WIDTH - 250, SCREEN_HEIGHT * 1/3))

# Dealer and player card "mats"
MAT_WIDTH, MAT_HEIGHT = 175, 250
dealer_mat = pygame.Surface((MAT_WIDTH,MAT_HEIGHT))
dealer_mat.fill((248,112,90))
dealer_mat_rect = dealer_mat.get_frect(midtop = (SCREEN_WIDTH/2, 30))
dealer_mat_label = REG_FONT.render("Dealer", True, "Black")
dealer_mat_label_rect = dealer_mat_label.get_frect(midtop = (SCREEN_WIDTH/2, 40))


def get_mat(index):
   player_mat = pygame.Surface((MAT_WIDTH,MAT_HEIGHT))
   player_mat.fill((207,118,74))
   gap = (SCREEN_WIDTH - len(players)* MAT_WIDTH) / (len(players) + 1)
   top_left_x = gap * (index + 1) + (index * 175)
   player_mat_rect = player_mat.get_frect(topleft = (top_left_x, 440))
   return [player_mat, player_mat_rect]


def draw_mat(players, index):
   screen.blit(get_mat(index)[0],get_mat(index)[1])
   player_mat_label = REG_FONT.render(f"{players[index].get_name()}", True, "Black")

   gap = (SCREEN_WIDTH - len(players)* MAT_WIDTH) / (len(players) + 1)
   top_left_x = gap * (index + 1) + (index * 175)

   player_mat_label_rect = player_mat_label.get_frect(midtop = (get_mat(index)[1].centerx, 450))
   screen.blit(player_mat_label, player_mat_label_rect)


while running:


   # event loop
   for event in pygame.event.get():


       # exit the game if the user clicks the red "X"
       if event.type == pygame.QUIT:
           running = False
      
       # while a game is currently active/being played
       elif game_active:


           # handles player turns
           if turn_tracker < len(players):
               # players can only make a move if their hand totals less than 21
               if players[turn_tracker].count_hand() < 21:
                   if hit_bttn.check_click() and cards_dealt:
                       players[turn_tracker].draw_card(deck.deal_card())
                       if players[turn_tracker].count_hand() >= 21: # check this for multi-player
                        turn_tracker += 1 
                   elif stay_bttn.check_click() and cards_dealt:
                       turn_tracker += 1
               # if bust or a natural blackjack, the turn is over
               else:
                   turn_tracker +=1
          
           # once every player has had a turn, the dealer goes
           elif turn_tracker == len(players):
               dealer_turn()
               # generates the result for each player and stores the surfaces to be displayed in a list
               for i in range(len(players)):
                   result_surf = get_round_result(players[i])
                   result_rect = result_surf.get_frect(center = (get_mat(i)[1].centerx, get_mat(i)[1].centery))
                   results.append((result_surf, result_rect))
               turn_tracker += 1
           else:
               # round is over
               game_active = False
                      
       else:
           # Pygame window is active, but a game is over
           # If a player wants to begin/continue to the next round, press space.
           if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
               if not players_enrolled:
                   enroll_players()
                   players_enrolled = True
              
               # Resets game variables
               reset_round(players, dealer, deck, results)
               cards_dealt = False
               turn_tracker = 0
               game_active = True


   # draw the game to the screen
   if not game_active:
       # title screen
       if rounds == 0:
           screen.fill((29,127,124))
           title = TITLE_FONT.render("BLACKJACK", True, "black")
           title_rect = title.get_frect(center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
           screen.blit(title, title_rect)


           caption = REG_FONT.render("Press SPACE to start", True, "black")
           caption_rect = caption.get_frect(center = (SCREEN_WIDTH/2,title_rect.bottom))
           screen.blit(caption, caption_rect)


   else:
       # these drawings occur every loop of the iteration so that they remain on the screen throughout the game


       # background colour
       screen.fill((29,127,124))


       # draws dealer mat            
       screen.blit(dealer_mat, dealer_mat_rect)
       screen.blit(dealer_mat_label, dealer_mat_label_rect)


       # draws player mats
       for i in range(len(players)):
           draw_mat(players,i)


       # starts a new round by dealing 2 cards to each player
       if not cards_dealt:
           rounds += 1
           deal_initial_cards(players, dealer, deck)
           cards_dealt = True


       # draws buttons
       hit_bttn.draw(screen)
       stay_bttn.draw(screen)


       # displays the dealer's hand  
       illustrate_hand(dealer, 562, dealer_mat_rect.top + 30)


       # displays each players hand and hand total 
       for i in range(len(players)):
               
               gap = (SCREEN_WIDTH - len(players)* MAT_WIDTH) / (len(players) + 1)
               top_left_x = gap * (i + 1) + (i * 175)

               illustrate_hand(players[i], get_mat(i)[1].left + 10, get_mat(i)[1].top + 30)
               illustrate_total(players[i], get_mat(i)[1].right - 20 , get_mat(i)[1].top + 20)
               illustrate_wins(players[i], get_mat(i)[1].centerx, get_mat(i)[1].bottom)
      
       # if round is over, display the results
       if turn_tracker > len(players):       
           illustrate_total(dealer, SCREEN_WIDTH/2 + 58, dealer_mat_rect.top + 20) # displays dealers total, now that their card isn't hidden
          
           # displays each player's results
           for(surf, rect) in results:
               screen.blit(surf, rect)

           # prompt to continue
           next_round_surf = REG_FONT.render("Press SPACE to continue to the next round. Click the red 'X' to exit.", True, "White")
           next_round_rect = next_round_surf.get_frect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
           screen.blit(next_round_surf, next_round_rect)


       # Displays the number of rounbds
       round_surf = REG_FONT.render(f"Round #{rounds}", True, "White")
       round_rect = round_surf.get_frect(topleft = (SCREEN_WIDTH - 100, 20))
       screen.blit(round_surf, round_rect)


   pygame.display.flip()
   clock.tick(150)


pygame.quit()