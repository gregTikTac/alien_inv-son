import sys  # ends game on commands player

import pygame  # contains functional


class AlienInvasion:
    """class for control resources and game behavior"""

    def __init__(self):
        """init game and create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode(1200, 800)  # call display (self.screen == surface)
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """start loop_game"""
        while True:     # event loop
            for event in pygame.event.get():  # tracking keyboard and mouse events (pygame.event == access for events)
                if event.type == pygame.QUIT:
                    sys.exit()

            """display the last drawn screen"""
            pygame.display.flip()


if __name__ == '__main__':
    """create instance and start game"""
    ai = AlienInvasion()
    ai.run_game()