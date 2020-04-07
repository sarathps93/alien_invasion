class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.game_active = False
        self.score = 0
        self.high_score = 0
        self.level = 1
        self.reset_stats()

    def reset_stats(self):
        # Initialise statistics that can change during the game
        self.ships_left = self.settings.ship_limit