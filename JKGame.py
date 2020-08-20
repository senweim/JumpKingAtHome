#!/usr/env/bin python
#   
# Game Screen
# 

import pygame 
import sys
import os
from settings import Settings
from spritesheet import SpriteSheet
from Background import Backgrounds
from King import King
from Babe import Babe
from Level import Levels
from Camera import Camera

class JKGame:
	""" Overall class to manga game aspects """
        
	def __init__(self):

		pygame.init()

		self.settings = Settings()

		self.clock = pygame.time.Clock()

		self.fps = int(os.environ.get("fps"))

		self.scale = int(os.environ.get("resolution"))
 
		self.bg_color = (0, 0, 0)

		self.screen = pygame.display.set_mode((int(os.environ.get("screen_width")), int(os.environ.get("screen_height"))), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE|pygame.SRCALPHA)

		self.fake_screen = self.screen.copy()

		self.fake_screen_x = 0

		self.levels = Levels(self.fake_screen) 

		self.king = King(self.fake_screen, self.levels)

		self.babe = Babe(self.fake_screen, self.levels)

		pygame.display.set_caption('Jump King At Home XD')

	def run_game(self):
 
		""" Start the main loop for the game """  
         
		while True:

			self.clock.tick(self.fps)
       
			self._check_events()

			self._update_features()

			self._update_screen()

	def _check_events(self):

		for event in pygame.event.get():

			if event.type == pygame.QUIT:

				sys.exit()

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_c:

					if os.environ["mode"] == "creative":

						os.environ["mode"] = "normal"

					else:

						os.environ["mode"] = "creative"

			if event.type == pygame.VIDEORESIZE:

				pygame.transform.scale(self.fake_screen, (event.w, event.h))

	def _update_features(self):

		self.levels.update_levels(self.king, self.babe)

	def _update_screen(self):

		self.fake_screen.fill(self.bg_color)

		self.levels.blit1()
		print(self.levels.current_level)
		self.king.blitme()

		self.babe.blitme()

		self.levels.blit2()

		pygame.display.set_caption(f"Jump King At Home XD - {self.clock.get_fps():.2f} FPS")

		self._shake_screen()

		self.screen.blit(self.fake_screen, (self.fake_screen_x, 0))

		pygame.display.update()

	def _shake_screen(self):

		try:

			if self.levels.levels[self.levels.current_level].shake:

				if self.levels.shake_var <= 150:

					self.fake_screen_x = 0

				elif self.levels.shake_var // 8 % 2 == 1:

					self.fake_screen_x = -self.scale

				elif self.levels.shake_var // 8 % 2 == 0:

					self.fake_screen_x = self.scale

			if self.levels.shake_var > 260:

				self.levels.shake_var = 0

			self.levels.shake_var += 1

		except:

			print("SHAKE ERROR")

if __name__ == "__main__":

	Game = JKGame()
	Game.run_game()