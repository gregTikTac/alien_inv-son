import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """class for control bullet"""

    def __init__(self, ai_game):
        """create bullet-object in current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        # create bullet in position (0,0) and assigned the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)  # rect=position bullet\
        # pygame.Rect = create bullet from koordinat 0

        self.rect.midtop = ai_game.ship.rect.midtop  # midtop bullet == midtop ship

        # bullet position saved in float format
        self.y = float(self.rect.y)

    def update(self):
        """moving bullet up on the screen"""
        # update bullet position in float format
        self.y -= self.settings.bullet_speed
        # update rectangle position
        self.rect.y = self.y

    def draw_bullet(self):
        """output bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
