import os 
import pygame

os.chdir('E:/Programming/GitHub/alien_invasion')

class Ship():
    def __init__(self, screen):
        """Initialize the ship and set its starting position"""
        self.screen = screen
        
        # Load the ship image and get its rect
        self.image = pygame.image.load('bmp/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
        
        
# Getting spaceship image from Pixabay
# https://pixabay.com/users/mongames-842983/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1414822