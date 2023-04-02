import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Will initialize game and create a screen object 
    pygame.init()
    setting = Settings()
    
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Make a ship
    ship = Ship(screen)
       
    # Start main loop for the game
    while True:
        gf.check_events() # Watch for keyboard and mouse events
        gf.update_screen(setting, screen, ship) # Update screen 
        
run_game()