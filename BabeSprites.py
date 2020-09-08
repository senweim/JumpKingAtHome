#!/usr/bin/env python
#
#
#
#

import pygame
import math
import collections
import os
from spritesheet import SpriteSheet

class Babe_Sprites():

	def __init__(self):

		self.filename = "images\\sheets\\ending_animations.png"

		self.spritesheet = SpriteSheet(self.filename)

		self.start_rect = (160, 0, 32, 32)

		self.babe_sprite_names = ["Babe_Kiss",
								"Babe_Stand1",
								"Babe_Stand2",
								"Babe_Stand3",
								"Babe_Crouch",
								"Babe_Fall",
								"Babe_Jump",
								"Babe_Land"]

		self.babe_images = {}

		self._load_images()

	def _load_images(self):

		images = self.spritesheet.load_grid(self.start_rect, 4, 2, -1)

		self.babe_images = dict(zip(self.babe_sprite_names, images))