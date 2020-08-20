#!/usr/bin/env python
#
#
#
#

import pygame
import re
import os
import collections
from settings import Settings

class Background():

	def __init__(self, filename):

		self.scale = int(os.environ.get("resolution"))

		self.image = self._load_image(filename)

		self.rect = self.image.get_rect()

	def _load_image(self, filename, colorkey = None):

		""" Load a specific image from a file """

		try:

			image = pygame.image.load(filename).convert_alpha()
			image = pygame.transform.scale(image, (image.get_width() * self.scale, image.get_height() * self.scale))

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
