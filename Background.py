#!/usr/bin/env python
#
#
#
#

import pygame
import re
import os
import collections

class Background():

	def __init__(self, filename):

		self.image = self._load_image(filename)

		self.x, self.y = 0, 0
		self.width, self.height = self.image.get_size()

	@property
	def rect(self):
		return pygame.Rect(self.x, self.y, self.width, self.height)
	
	def _load_image(self, filename, colorkey = None):

		""" Load a specific image from a file """

		try:

			image = pygame.image.load(filename).convert_alpha()

		except pygame.error as e:
			print(f'Unable To Load Image: {filename}')
			raise SystemExit(e)

		return image

	def blitme(self, screen):

		screen.blit(self.image, self.rect)

class Backgrounds():

	def __init__(self, directory):

		pygame.init()

		self.directory = directory

		self.backgrounds = collections.defaultdict()

		self._load_background_sprites()

	def _load_background_sprites(self):

		for filename in sorted(os.listdir(self.directory), key = lambda filename: int(re.search(r'\d+', filename).group())):
			
			bg = Background(os.path.join(self.directory, filename))

			level = int(re.search(r'\d+', filename).group()) - 1

			self.backgrounds[level] = bg

if __name__ == "__main__":

	background = Backgrounds(pygame.display.set_mode((480, 360)), 's', "BG")
