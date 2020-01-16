import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ss_game):
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        
        self.image = pygame.image.load(self.settings.alien_image)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)