#!/usr/bin/env python
#
#
#
#

import pygame
import collections
import os
import re
import sys

class HiddenWalls:

	def __init__(self):

		self.directory = "hiddenwalls"

		self.names = {"6_hidden_wall1.png" : (303, 223),
					"6_hidden_wall2_1.png" : (382, 47),
					"6_hidden_wall2_2.png" : (288, 47),
					"6_hidden_wall3.png" : (167, 0),
					"7_hidden_wall1_1.png" : (152, 279),
					"7_hidden_wall1_2.png" : (240, 303),
					"21_hidden_wall1.png" : (7, 287)}

		self.hiddenwalls = collections.defaultdict()

		self._load_hiddenwalls()

	def _load_hiddenwalls(self):

		self.hiddenwalls[6] = [HiddenWall(*self.names["6_hidden_wall1.png"], self.directory, "6_hidden_wall1.png"),
							HiddenWall(*self.names["6_hidden_wall2_2.png"], self.directory, "6_hidden_wall2_2.png"),
							HiddenWall(*self.names["6_hidden_wall2_1.png"], self.directory, "6_hidden_wall2_1.png"),
							HiddenWall(*self.names["6_hidden_wall3.png"], self.directory, "6_hidden_wall3.png")]

		self.hiddenwalls[7] = [HiddenWall(*self.names["7_hidden_wall1_2.png"], self.directory, "7_hidden_wall1_2.png"),
							HiddenWall(*self.names["7_hidden_wall1_1.png"], self.directory, "7_hidden_wall1_1.png")]

		self.hiddenwalls[21] = [HiddenWall(*self.names["21_hidden_wall1.png"], self.directory, "21_hidden_wall1.png")]

class HiddenWall:

	def __init__(self, x, y, directory, file):

		self.image = pygame.image.load(f"{directory}\\{file}")

		self.fake = pygame.Surface((self.image.get_width(), self.image.get_height())).convert()

		self.fake.set_colorkey((0, 0, 0))

		self.fake.blit(self.image, (0, 0))

		self.found_channel = pygame.mixer.Channel(6)

		self.found_audio = pygame.mixer.Sound("Audio\\Misc\\new_location.wav")

		self.found_audio.set_volume(1.0)

		self.found = False

		self.x, self.y = x, y

		self.mask = pygame.mask.from_surface(self.image)

		self.opacity = 255

	def blitme(self, screen):

		self.fake.set_alpha(self.opacity)

		screen.blit(self.fake, (self.x, self.y))

	def check_collision(self, king):

		king.mask = pygame.mask.from_surface(king.current_image)

		if king.mask.overlap(self.mask, (self.x - king.x, self.y - king.y)):

			if not self.found:

				self.found_channel.play(self.found_audio)

				self.found = True

			if self.opacity > 0:
				self.opacity -= 55


		else:

			if self.opacity < 255:

				self.opacity += 55


