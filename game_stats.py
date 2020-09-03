#game_stats.ry
class GameStats():
    """ Statistics monitoring"""
    def __init__(self, ai_settings):
        """ Init statistic"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
    def reset_stats(self):
        """ Init changes stats"""
        self.ships_left = self.ai_settings.ship_limit
    