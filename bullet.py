import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ Class for bulllet management """
    def __init__(self, ai_settings, screen, ship):
        """ Create bullet object in ship position"""
        super(Bullet, self).__init__()
        self.screen = screen
        
        # Making bullet at position (0,0) and set right position
        self.rect = pygame.Rect(0,0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # Bullet position to float
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        """ Move bullet up"""
        # Update position in float
        self.y -= self.speed_factor
        # Ipdate rect position
        self.rect.y = self.y
    def draw_bullet(self):
        """ Draw bullet """
        pygame.draw.rect(self.screen, self.color, self.rect)
    