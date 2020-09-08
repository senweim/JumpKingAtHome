#!/usr/bin/env python
#
#
#
#

import pygame
import math
import os

class Wind:

	def __init__(self, screen):

		self.screen = screen

		self.wind_var = 0

		self.x, self.y, self.width, self.height = 0, 0, self.screen.get_width(), self.screen.get_height()

	@property
	def rect(self):
		return pygame.Rect(self.x, self.y, self.width, self.height)
	
	def calculate_wind(self, king):

		wind = math.sin(self.wind_var) * (2.5) ** 2

		self.wind_var += math.pi / 500

		self.x += wind

		return wind
