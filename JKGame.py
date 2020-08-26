#!/usr/env/bin python
#   
# Game Screen
# 

import pygame 
import sys
import os
import inspect
import pickle
from settings import Settings
from spritesheet import SpriteSheet
from Background import Backgrounds
from King import King
from Babe import Babe
from Level import Levels
from Menu import Menus
from Camera import Camera
from Start import Start

class JKGame:
	""" Overall class to manga game aspects """
        
	def __init__(self):

		pygame.init()

		self.settings = Settings()

		self.clock = pygame.time.Clock()

		self.fps = int(os.environ.get("fps"))
 
		self.bg_color = (0, 0, 0)

		self.screen = pygame.display.set_mode((int(os.environ.get("screen_width")), int(os.environ.get("screen_height"))), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE|pygame.SRCALPHA)

		pygame.display.set_icon(pygame.image.load("icon.png"))

		self.game_screen = self.screen.copy()

		self.game_screen_x = 0

		self.levels = Levels(self.game_screen)

		self.king = King(self.game_screen, self.levels)

		self.babe = Babe(self.game_screen, self.levels)

		self.menus = Menus(self.game_screen, self.levels, self.king)

		self.start = Start(self.game_screen, self.menus)

		pygame.display.set_caption('Jump King At Home XD')

	def run_game(self):
 
		""" Start the main loop for the game """  
         
		while True:

			self.clock.tick(self.fps)
    
			self._check_events()

			if not os.environ["pause"]:

				self._update_gamestuff()

			self._update_gamescreen()

			self._update_guistuff()

			pygame.display.update()

	def _check_events(self):

		for event in pygame.event.get():

			if event.type == pygame.QUIT:

				sys.exit()

			if event.type == pygame.KEYDOWN:

				self.menus.check_events(event)

				if event.key == pygame.K_c:

					if os.environ["mode"] == "creative":

						os.environ["mode"] = "normal"

					else:

						os.environ["mode"] = "creative"
					
			if event.type == pygame.VIDEORESIZE:

				self.screen = pygame.display.set_mode((event.w, event.h), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE|pygame.SRCALPHA)

	def _update_gamestuff(self):

		self.levels.update_levels(self.king, self.babe)

	def _update_guistuff(self):

		if self.menus.current_menu:

			self.menus.update()

		if not os.environ["gaming"]:

			self.start.update()

	def _update_gamescreen(self):

		pygame.display.set_caption(f"Jump King At Home XD - {self.clock.get_fps():.2f} FPS")

		self.game_screen.fill(self.bg_color)

		if os.environ["gaming"]:

			self.levels.blit1()

		if os.environ["active"]:

			self.king.blitme()

		if os.environ["gaming"]:
			self.babe.blitme()

		if os.environ["gaming"]:

			self.levels.blit2()

		if os.environ["gaming"]:

			self._shake_screen()

		if not os.environ["gaming"]:

			self.start.blitme()

		if self.menus.current_menu:

			self.menus.blitme()

		self.screen.blit(pygame.transform.scale(self.game_screen, (self.screen.get_width(), self.screen.get_height())), (self.game_screen_x, 0))

	def _shake_screen(self):

		try:

			if self.levels.levels[self.levels.current_level].shake:

				if self.levels.shake_var <= 150:

					self.game_screen_x = 0

				elif self.levels.shake_var // 8 % 2 == 1:

					self.game_screen_x = -1

				elif self.levels.shake_var // 8 % 2 == 0:

					self.game_screen_x = 1

			if self.levels.shake_var > 260:

				self.levels.shake_var = 0

			self.levels.shake_var += 1

		except:

			print("SHAKE ERROR")

if __name__ == "__main__":

	Game = JKGame()
	Game.run_game()