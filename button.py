import pygame

pygame.init()

# if button size is constant, then we don't care about that as a a parameter 
class Button:
    font = pygame.font.Font(None, 30)

    def __init__(self, label, bttn_colour, font_colour, center):
        self._label = label
        self._clicked = False
        self._center = center
        self._enabled = True

        # create surfaces
        self._bttn_surf = pygame.Surface((175, 80))
        self._bttn_surf.fill(bttn_colour)
        self._bttn_rect = self._bttn_surf.get_frect(center = self._center)

        self._bttn_text = Button.font.render(self._label, True, font_colour)
        self._bttn_text_rect = self._bttn_text.get_frect(center = self._center)

    def draw(self, surface):
        surface.blit(self._bttn_surf, self._bttn_rect)
        surface.blit(self._bttn_text, self._bttn_text_rect)

    def check_click(self):
        if self._enabled:
            mouse_pos = pygame.mouse.get_pos()
            left_click = pygame.mouse.get_pressed()[0]
            if left_click and self._bttn_rect.collidepoint(mouse_pos) and not self._clicked:
                self._clicked = True
                print("CLICKED!")
                return True # Button was clicked
            
            if not left_click:
                self._clicked = False # Resets state (only allows a new click once the button has been released)

            return False

    def set_enabled(self, state):
        self._enabled = state
    
    def get_enabled(self):
        return self._enabled
    



