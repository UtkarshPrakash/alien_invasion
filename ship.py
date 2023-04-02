import os 
import pygame

class Ship():
    def __init__(self, screen):
        """Initialize the ship and set its starting position"""
        self.screen = screen
        
        # Load the ship image and get its rect
        self.image = pygame.image.load('bmp/ship.bmp')
        self.image = pygame.transform.scale(self.image, (40, 90))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # Movement Flag
        self.moving_right = False
        
    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_right:
            self.rect.centerx += 1
        
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
        
        
# Getting spaceship image from Pixabay
# https://pixabay.com/users/mongames-842983/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1414822
