import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
#from alien import Alien
import game_functions as gf

def run_game():
    # Init game and create screen
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
(ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Ship creating
    ship = Ship(ai_settings, screen)
    # Creating group of bullets
    bullets = Group()
    # Creating alien
    #alien = Alien(ai_settings, screen)
    aliens = Group()
    # Creating group of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # First circle start
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
            
        
run_game()