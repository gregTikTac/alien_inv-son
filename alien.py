import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """class for one alien"""

    def __init__(self, ai_game):
        """init alien and set him start position"""
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # everyone alian starting in the left-up coal
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # saved alien position
        self.x = float(self.rect.x)