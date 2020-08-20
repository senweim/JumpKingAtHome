#!/usr/bin/env python
#
#
#
#

import pygame
import os
import collections
import re

class BackgroundAudio:

	def __init__(self):

		self.directory = "Audio\\Background"

		self.audio = collections.defaultdict()

		self.level_audio = collections.defaultdict()

		self._load_audio()

		self._load_levels()

	def _load_levels(self):

		self.level_audio[0] = [self.audio["Nature bg"], self.audio["Small fire and stream"], None, None]

		self.level_audio[1] = [self.audio["Nature bg"], None, None, None]

		self.level_audio[2] = [self.audio["Nature bg"], None, None, None]

		self.level_audio[3] = [self.audio["Nature bg"], None, self.audio["Red tree"], None]		

		self.level_audio[4] = [self.audio["Nature bg"], None, self.audio["Red tree"], None]

		self.level_audio[5] = [self.audio["Nature bg"], self.audio["Sewer"], self.audio["Dungeon"], None]

		self.level_audio[6] = [None, self.audio["Sewer"], self.audio["Dungeon"], None]

		self.level_audio[7] = [None, self.audio["Sewer"], self.audio["Dungeon"], None]

		self.level_audio[8] = [self.audio["Sewer cage rain"], self.audio["Sewer"], self.audio["Dungeon"], None]

		self.level_audio[9] = [self.audio["Light rain"], self.audio["Sewer"], self.audio["Dungeon"], self.audio["Castlesong"]]

		self.level_audio[10] = [self.audio["Hard rain and fire"], None, None, self.audio["Castlesong"]]

		self.level_audio[11] = [self.audio["Hard rain and fire"], None, None, self.audio["Castlesong"]]		

		self.level_audio[12] = [self.audio["Hard rain and fire"], None, None, self.audio["Castlesong"]]

		self.level_audio[13] = [self.audio["Wind 1"], None, None, self.audio["Castlesong"]]

		self.level_audio[14] = [self.audio["City 1"], None, None, self.audio["Merchant loop"]]

		self.level_audio[15] = [self.audio["City 1"], None, None, self.audio["Merchant loop"]]		

		self.level_audio[16] = [self.audio["City 1"], None, None, None]		

		self.level_audio[17] = [self.audio["City 1"], None, None, None]		

		self.level_audio[18] = [self.audio["City 1"], None, None, None]		

		self.level_audio[19] = [self.audio["towers 1"], None, None, None]

		self.level_audio[20] = [self.audio["towers 1"], None, None, None]

		self.level_audio[21] = [self.audio["towers 1"], None, None, None]

		self.level_audio[22] = [self.audio["windy towers 2"], None, None, None]	

		self.level_audio[23] = [self.audio["windy towers 2"], None, None, None]	

		self.level_audio[24] = [self.audio["windy towers 2"], None, None, None]	

		self.level_audio[25] = [self.audio["snowy windy"], None, None, None]

		self.level_audio[26] = [self.audio["snowy windy"], None, None, None]

		self.level_audio[27] = [self.audio["snowy windy"], None, None, None]

		self.level_audio[28] = [self.audio["snowy windy"], None, None, None]

		self.level_audio[29] = [self.audio["snowy windy"], None, None, None]

		self.level_audio[29] = [self.audio["snowy windy"], None, None, None]

		self.level_audio[30] = [self.audio["snowy windy"], None, None, None]

		self.level_audio[31] = [self.audio["snowy windy"], self.audio["Cathedral"], None, None]

		self.level_audio[32] = [None, self.audio["Cathedral"], None, None]

		self.level_audio[33] = [None, self.audio["Cathedral"], None, None]		

		self.level_audio[34] = [None, self.audio["Cathedral"], None, None]		

		self.level_audio[35] = [None, self.audio["Cathedral"], self.audio["synth drone"], None]

		self.level_audio[36] = [None, self.audio["test song ice"], self.audio["Ice wind new"], None]

		self.level_audio[37] = [None, self.audio["test song ice"], self.audio["Ice wind new"], None]

		self.level_audio[38] = [None, self.audio["test song ice"], self.audio["Ice wind new"], None]

		self.level_audio[39] = [self.audio["Final Climb"], self.audio["Earthquake"], None, None]

		self.level_audio[40] = [self.audio["Final Climb"], self.audio["Earthquake"], None, None]

		self.level_audio[41] = [self.audio["Final Climb"], self.audio["Earthquake"], None, None]

		self.level_audio[42] = [self.audio["ending_jingle"], self.audio["Earthquake"], None, None]

	def _load_audio(self):

		for file in os.listdir(f"{self.directory}"):

			audio = pygame.mixer.Sound(f"{self.directory}\\{file}")

			audio.set_volume(1.0)

			self.audio[re.match(r"[^.]*", file).group()] = audio







