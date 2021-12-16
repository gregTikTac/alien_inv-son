class Settings():
    """class for storing setting game Alien_ Invasion"""

    def __init__(self):
        """init setting game"""
        # display parameters
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # settings ship
        self.ship_speed = 1.5

        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
