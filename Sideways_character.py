#William Brown

import pygame

class Ship():
    
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings
        
        #Load the ship image and get its rect.
        self.image = pygame.image.load('sideways_spaceship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #Start each new ship on the left hand side middle of the screen.
        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery
        
        #Store a decimal value for the ship's center.
        self.center = float(self.rect.centery)
        
        #Movement flags.
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.center -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += 1
            
        #Update rect object from self.center.
        self.rect.centery = self.center
        
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)