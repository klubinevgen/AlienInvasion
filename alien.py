# alien.py
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ Single alien class"""
    def __init__(self, ai_settings, screen):
        """ Init one alien and set its position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Load alien image and set rect atrubutes
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # Every new alien shows in left bottom
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Saves exact position
        self.x = float(self.rect.x)
    def blitme(self):
        """ Shows alien in current state"""
        self.screen.blit(self.image, self.rect)
    def update(self):
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x
    def check_edges(self):
        """ Return true if alien on edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True