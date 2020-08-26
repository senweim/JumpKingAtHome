#!/usr/bin/env python
#
#
#
#

import pygame
import os
from spritesheet import SpriteSheet

class King_Particle:

	def __init__(self, image, rows, image_count, size):

		self.start_rect = (0, 0, size, size)

		self.blit_rect = None

		self.blit_counter = 0

		self.blit_interval = 2

		self.spritesheet = SpriteSheet(image)

		self.images = self.spritesheet.load_grid(self.start_rect, rows, image_count, -1)

	def blitme(self, screen):

		if self.blit_rect:

			screen.blit(self.images[self.blit_counter // self.blit_interval], self.blit_rect)

			self.blit_counter += 1

			if self.blit_counter == self.blit_interval * len(self.images):

				self.blit_counter = 0

				self.blit_rect = None

		else:

			self.reset()

	def reset(self):

		self.blit_counter = 0

		self.blit_rect = None

	def play(self, rect):

		self.blit_rect = rect






