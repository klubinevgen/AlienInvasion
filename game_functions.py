# game_functions
import sys
import pygame
from time import sleep

from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """ Reacts on key pressing"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
                
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, stats, play_button, ship, aliens,
                 bullets):
    """ Working on keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button,
                              ship, aliens, bullets, mouse_x, mouse_y)
            
def check_play_button(ai_settings, screen, stats, play_button, ship, aliens,
                      bullets, mouse_x, mouse_y):
    """ Starts new game when play is pressed """
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        if play_button.rect.collidepoint(mouse_x, mouse_y):
            # Cursor hide
            pygame.mouse.set_visible(False)
            # Clear statistics
            stats.reset_stats()
            stats.game_active = True
            # Clear aliens and bullets
            aliens.empty()
            bullets.empty()
            # Creating new fleet and setting ship
            create_fleet(ai_settings, screen, ship, aliens)
            ship.center_ship()

def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button):
    """ Refresh image and shows new screen"""
    # Every cicle redraw screen
    screen.fill(ai_settings.bg_color)
    # Every bullets draws after ships and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # Play button shows when inactive
    if not stats.game_active:
        play_button.draw_button()
    
    # Shows last draw screen
    pygame.display.flip()

def fire_bullet(ai_settings, screen, ship, bullets):
    """ Fires if no limit exceed"""
    if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """ Updates bullet position delete old bullets"""
    # Bullets update
    bullets.update()
    # Delete outranged bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    # Checking for aliens hit
    # If hit, remove alien and bullet
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)
    if len(aliens) == 0:
        # Clear bullets and creating new fleet
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
def get_number_aliens_x(ai_settings, alien_width):
    """ Get numbers of aliens in a row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows (ai_settings, ship_height, alien_height):
    """ Get rows number for screen"""
    available_space_y = (ai_settings.screen_height -
                         (3*alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
    
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)            
            
def create_fleet(ai_settings, screen, ship, aliens):
    """ Creating aliens fleet"""
    # Making alien and qnty in row calc
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                  alien.rect.height)
    
    # Creating first row
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,
                         row_number)
        # Make alien and stand in row
        
 
def check_fleet_edges(ai_settings, aliens):
    """ Reacts on alien on edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
def change_fleet_direction(ai_settings, aliens):
    """ Move fleet down"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """ Cheks for fleet on edge and move it down"""
    check_fleet_edges(ai_settings, aliens)
    """ Updates aliens positions"""
    aliens.update()
    # checking for collisions ship-alien
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    # Checking for aliens on bottom edge
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """ Works on ship-alien collide"""
    if stats.ships_left > 0:
        # Discrase ships_left
        stats.ships_left -= 1
        # Empty aliens and bullets list
        aliens.empty()
        bullets.empty()
        # Creating new fleet and set ship in center
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # Pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """ Checks if aliens reach bottom"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Происходит то же, что при столкновении с кораблем
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break