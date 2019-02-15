#William Brown

class Settings():
   """#Stores all settings for game."""
    
   def __init__(self):
        """initialize the game's settings."""
        #Screen Settings.
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (0, 0, 0)
        
        #Ship settings.
        self.ship_speed_factor = 2

        #Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = 255, 255, 255
        self.bullets_allowed = 3
        