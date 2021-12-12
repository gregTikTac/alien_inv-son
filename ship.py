import pygame


class Ship():
    """class for control ship"""

    def __init__(self, ai_game):
        """init ship and sets starting position"""
        self.screen = ai_game.screen  # window assigned ship  to make it easier to handle
        self.screen_rect = ai_game.screen.get_rect()  # allows you to place the ship in the desired position

        # loading img ship and  receive  rectangle
        self.image = pygame.image.load('images/ship.bmp')  # load img
        self.rect = self.image.get_rect()  # attribute (rect) for ship position

        # each ship appears at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # flag for moving
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """updates the ship's position with the flag"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """draw ship in current position"""
        self.screen.blit(self.image, self.rect)