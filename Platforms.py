#!/usr/bin/env python
#
#
#
#

import pygame

class Rectangles:

	def __init__(self):

		self.level_1 = [(0, 185, 128, 175),
						(352, 185, 128, 175),
						(185, 40, 110, 50),
						(128, 330, 224, 30)]

class Platforms():

	def __init__(self, screen):

		self.screen = screen

		self.rectangles = Rectangles()

		self.platforms = [pygame.Rect(rectangle) for rectangle in self.rectangles.level_1]

	def blitme(self):

		for platform in self.platforms:

			pygame.draw.rect(self.screen, (255, 0, 0), platform, 1)
