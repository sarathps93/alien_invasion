import pygame

class Ship:
    def __init__(self, ai_game):
        # Initialise the ship and it's starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get it's rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        #Start each ship at the bottom centre of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        #Draw ship at it's current location
        self.screen.blit(self.image, self.rect)

