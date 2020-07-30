#!/usr/bin/env python
#
#
#
#

import pygame

class Background(pygame.sprite.Sprite):

	def __init__(self, filename):

		super().__init__() 

		self.image = self._load_image(filename)

		self.rect = self.image.get_rect()

	def _load_image(self, filename, colorkey = None):

		""" Load a specific image from a file """

		try:
			image = pygame.image.load(filename).convert_alpha()
		except pygame.error as e:
			print(f'Unable To Load Image: {filename}')
			raise SystemExit(e)

		return image

class Backgrounds(pygame.sprite.Group):

	def __init__(self, screen, x, y, *filenames):

		super().__init__()

		pygame.init()

		self.screen = screen

		self.x, self.y = x, y

		self._load_background_sprites(filenames)

	def blitme(self):

		self.draw(self.screen)

	def _load_background_sprites(self, filenames):

		for filename in filenames:

			self.add(Background(filename))








		
