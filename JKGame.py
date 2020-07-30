#!/usr/env/bin python
#
# Game Screen
#
#

import pygame
import sys
from settings import Settings
from spritesheet import SpriteSheet
from Background import Backgrounds
from King import King
from Platforms import Platforms

class JKGame:
	""" Overall class to manga game aspects """
        
	def __init__(self):

		pygame.init()

		self.settings = Settings()

		self.clock = pygame.time.Clock()

		self.fps = self.settings.fps

		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

		self.king = King(self.screen)

		self.platforms = Platforms(self.screen)

		self.background = Backgrounds(self.screen, 0, 0, "bg4.png")

		self.midground = Backgrounds(self.screen, 0, 0, "1.png")

		self.foreground = Backgrounds(self.screen, 0, 0, "fg1.png")

		pygame.display.set_caption('Jump King At Home XD')

	def run_game(self):

		""" Start the main loop for the game """

		while True:

			self.clock.tick(self.fps)

			self._check_events()

			self.king.update(self.platforms.platforms)

			self._update_screen()

	def _check_events(self):

		for event in pygame.event.get():

			if event.type == pygame.QUIT:

				sys.exit()

		self.king.check_controls()

	def _update_screen(self):

		self.screen.fill((self.settings.bg_color))

		self.background.blitme()

		self.midground.blitme()

		self.king.blitme()

		self.foreground.blitme()

		#self.platforms.blitme()

		pygame.display.flip()

if __name__ == "__main__":

	Game = JKGame()
	Game.run_game()