# settings.py
class Settings():
    """ Setting for whole game """
    def __init__(self):
        """ Game settings init"""
        # Screen parameters
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 3.5
        # Bullet parameters
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # Alien paremeters
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet direction = 1 means right: -1 ,eans left
        self.fleet_direction = 1