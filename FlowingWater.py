#!/usr/bin/env python
#
#
#
#

import pygame
import collections
from spritesheet import SpriteSheet

class Props:

	def __init__(self):

		self.Bonfire = Bonfire()

		self.FlowingWater = FlowingWater()


class Bonfire:

	def __init__(self):

		self.filename = "props\\Bonfire.png"

		self.spritesheet = SpriteSheet(self.filename)

		self.start_rect = (0, 0, 32, 32)

		self.x, self.y = 200, 200

		self.blit_counter = 0

		self.bonfire_images = collections.defaultdict()

		self._load_images()

	def _load_images(self):

		for index, image in enumerate(self.spritesheet.load_strip(self.start_rect, 3, -1)):

			self.bonfire_images[f"Flicker{index + 1}"] = image


	def blitme(self, screen):

		if self.blit_counter <= 10:
			screen.blit(self.bonfire_images["Flicker1"], (self.x, self.y))

		elif self.blit_counter <= 20:
			screen.blit(self.bonfire_images["Flicker2"], (self.x, self.y))

		elif self.blit_counter <= 30:
			screen.blit(self.bonfire_images["Flicker3"], (self.x, self.y))

			if self.blit_counter == 30:

				self.blit_counter = 0

		self.blit_counter += 1


class FlowingWater:

	def __init__(self):

		self.filename = "props\\1_water.png"

		self.spritesheet = SpriteSheet(self.filename)

		self.start_rect = [(0, 0 442, 75), (0, 75, 442, 75)]

		self.x, self.y = 300, 100

		self.blit_counter = 0

		self.water_images = []

		self._load_images(self)

	def _load_images(self):

		self.water_images.append(self.spritesheet.image_at(self.start_rect[0]))
		self.water_images.append(self.spritesheet.image_at(self.start_rect[1]))

	def blitme(self, screen):

		if self.blit_counter <= 10:
			screen.blit(self.water_images[0], (self.x, self.y))

		elif self.blit_counter <= 20:
			screen.blit(self.water_images[1], (self.x, self.y))

			if self.blit_counter == 20:

				self.blit_counter = 0

		self.blit_counter += 1
