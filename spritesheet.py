#!/usr/bin/env python
#
#
#
#

import pygame
import os

class SpriteSheet:

	""" Represents spritesheets """

	def __init__(self, filename):

		""" Load the sheet """

		pygame.init()

		#try:
		self.sheet = pygame.image.load(filename).convert_alpha()

		#except pygame.error as e:
		#	print(f"Unable to load spritesheet image: {filename} ")
		#	raise SystemExit(e)

	def image_at(self, rectangle, colorkey = None):

		""" Load a specific image from a specific rectangle."""

		rect = pygame.Rect(rectangle)

		image = pygame.Surface(rect.size, pygame.SRCALPHA).convert_alpha()

		image.blit(self.sheet, (0, 0), rect)

		# if colorkey is not None:
		# 	if colorkey == -1:
		# 		colorkey = image.get_at((0, 0))

			# image.set_colorkey(colorkey, pygame.RLEACCEL)

		return image

	def images_at(self, rects, colorkey = None):

		""" Load a whole bunch of images and return them as a list """

		return [self.image_at(rect, colorkey) for rect in rects]

	def load_strip(self, rect, image_count, colorkey = None):
		""" Load a whole strip of images, and return them as a list """

		tups = [(rect[0] + rect[2] * x, rect[1], rect[2], rect[3]) for x in range(image_count)]

		return self.images_at(tups, colorkey)

	def load_column(self, rect, image_count, colorkey = None):
		""" Load a whole column of images, and return them as a list """

		tups = [(rect[0], rect[1] + rect[3] * y, rect[2], rect[3]) for y in range(image_count)]

		return self.images_at(tups, colorkey)

	def load_grid(self, rect, image_count, col_count, colorkey = None):

		images = []

		for y in range(col_count):

			tups = [(rect[0] + rect[2] * x, rect[1] + rect[3] * y, rect[2], rect[3]) for x in range(image_count)]
			images.extend(self.images_at(tups, colorkey))

		return images

if __name__ == "__main__":

	jumpking_spritesheet = SpriteSheet("test.jfif")