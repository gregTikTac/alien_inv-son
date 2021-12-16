import sys  # ends game on commands player
import pygame  # contains functional
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """class for control resources and game behavior"""

    def __init__(self):
        """init game and create game resources"""
        pygame.init()
        self.settings = Settings()  # instance class Setting

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((1200, 800))  # call display (self.screen == surface)
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)  # create instance
        self.bullets = pygame.sprite.Group()  # bullet group

    def run_game(self):
        """start loop_game"""
        while True:
            self._check_events()  # call method
            self.ship.update()
            self.bullets.update()  # for everyone bullets
            self._update_screen()  # call method

    def _check_events(self):
        """handles keystrokes and mouse events"""
        for event in pygame.event.get():  # tracking keyboard and mouse events (pygame.event == access for events)
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # if push bottom (event = keydown)
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """reacts to keystrokes"""
        if event.key == pygame.K_RIGHT:  # test bottom "->"
            self.ship.moving_right = True  # move ship right (if push bottom "->")
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:  # "space" for shots
            self._fire_bullet()

    def _check_keyup_events(self, event):
        "Reacts when keys are released"
        if event.key == pygame.K_RIGHT:  # "->"
            self.ship.moving_right = False  # moving = false
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """create new bullet and adding in group bullets"""
        new_bullet = Bullet(self)  # exzempliar bullet
        self.bullets.add(new_bullet)

    def _update_screen(self):
        """update image and show new window"""
        self.screen.fill(self.settings.bg_color)  # on each pass of the loop, color is drawn
        self.ship.blitme()  # draw ship in window
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()  # display the last drawn screen"


if __name__ == '__main__':
    """create instance and start game"""
    ai = AlienInvasion()
    ai.run_game()
