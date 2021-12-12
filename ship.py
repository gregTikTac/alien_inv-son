import pygame


class Ship():
    """class for control ship"""

    def __init__(self, ai_game):
        """init ship and sets starting position"""
        self.screen = ai_game.screen  # window assigned ship  to make it easier to handle
        self.screen_rect = ai_game.screen.get_rect()  # allows you to place the ship in the desired position
        self.settings = ai_game.settings  # create attribute Setting, for use def update

        # loading img ship and  receive  rectangle
        self.image = pygame.image.load('images/ship.bmp')  # load img
        self.rect = self.image.get_rect()  # attribute (rect) for ship position

        # each ship appears at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # saving float koordinat ship
        self.x = float(self.rect.x)

        # flag for moving
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """updates the ship's position with the flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:  # self.rect.right = edge of the screen
            self.rect.x += self.settings.ship_speed  # update atr x, but no rect
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed

        # update atr rect
        self.rect = self.x

    def blitme(self):
        """draw ship in current position"""
        self.screen.blit(self.image, self.rect)