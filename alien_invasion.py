import sys  # ends game on commands player
import pygame  # contains functional
from setting import Setting
from ship import Ship


class AlienInvasion:
    """class for control resources and game behavior"""

    def __init__(self):
        """init game and create game resources"""
        pygame.init()
        self.setting = Setting()  # instance class Setting

        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        self.screen = pygame.display.set_mode((1200, 800))  # call display (self.screen == surface)
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)  # create instance

    def run_game(self):
        """start loop_game"""
        while True:
            self._check_events()  # call method
            self._update_screen()  # call method

            #  draw window
    def _check_events(self):
        """handles keystrokes and mouse events"""
        for event in pygame.event.get():  # tracking keyboard and mouse events (pygame.event == access for events)
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """update image and show new window"""
        self.screen.fill(self.setting.bg_color)  # on each pass of the loop, color is drawn
        self.ship.blitme()  # draw ship in window

        """display the last drawn screen"""
        pygame.display.flip()


if __name__ == '__main__':
    """create instance and start game"""
    ai = AlienInvasion()
    ai.run_game()
