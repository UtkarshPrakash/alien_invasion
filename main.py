import sys
import pygame
from settings import Settings


def run_game():
    # Will initialize game and create a screen object 
    pygame.init()
    setting = Settings()
    
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
       
    # Start main loop for the game
    while True:
        
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        screen.fill(setting.bg_color)
        
        # Makes the most recently drawn screen visible
        pygame.display.flip()
        
run_game()