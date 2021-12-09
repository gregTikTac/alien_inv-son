import sys  # ends game on commands player

import pygame  # contains functional


class AlienInvision:
    """class for control resources and game behavior"""

    def __init__(self):
        """init game and create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode(1200, 800)  # call display (self.screen == surface)
        pygame.display.set_caption("Alien Invasion")
