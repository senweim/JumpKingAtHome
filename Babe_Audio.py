#!/usr/bin/env python
#
#
#
#

import pygame
import os
import re
import collections

class Babe_Audio:

	def __init__(self):

		self.directory = "Audio"

		self.audio = collections.defaultdict()

		self._load_audio("Babe")

	def _load_audio(self, file):

		for audio in os.listdir(f"{self.directory}\\{file}"):

			a = pygame.mixer.Sound(f"{self.directory}\\{file}\\{audio}")

			a.set_volume(0.5)

			self.audio[re.match(r"[^.]*", audio).group()] = a
