import sys

import	pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	# Start game create screen
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Sean's Alien invasion")


	ship = Ship(screen, ai_settings)
	#set background colors
	#bg_color = (0, 0, 255)

	while True:

		#Watch for keyboard/mouse events
		gf.check_events(ship)
		ship.update()
		gf.update_screen(ai_settings, screen, ship)

run_game()