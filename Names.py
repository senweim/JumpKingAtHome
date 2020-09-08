#!\usr\bin\env python
#
#
#
#

import pygame
import os
import sys
import collections

class Names:

	def __init__(self):

		self.font = pygame.font.Font("Fonts\\ttf_pixolde_bold.ttf", 16)

		self.small_font = pygame.font.Font("Fonts\\ttf_pixolde_bold.ttf", 12)

		self.audio = pygame.mixer.Sound("Audio\\Misc\\new_location.wav")

		self.audio.set_volume(1.0)

		self.channel = pygame.mixer.Channel(8)

		self.names = collections.defaultdict()

		self._load_names()

		self.active = False

		self.blit_type = None

		self.blit_name = None

		self.opacity = 255

	def _load_names(self):

		self.names[1] = " REDCROWN WOODS "

		self.names[2] = " REDCROWN WOODS "

		self.names[3] = " REDCROWN WOODS "

		self.names[4] = " REDCROWN WOODS "

		self.names[5] = " COLOSSAL DRAIN "

		self.names[6] = " COLOSSAL DRAIN "

		self.names[7] = " COLOSSAL DRAIN "

		self.names[8] = " COLOSSAL DRAIN "

		self.names[9] = " COLOSSAL DRAIN "

		self.names[10] = " FALSE KINGS' KEEP "

		self.names[11] = " FALSE KINGS' KEEP "

		self.names[12] = " FALSE KINGS' KEEP "

		self.names[13] = " FALSE KINGS' KEEP "

		self.names[14] = " BARGAINBURG "

		self.names[15] = " BARGAINBURG "

		self.names[16] = " BARGAINBURG "

		self.names[17] = " BARGAINBURG "

		self.names[18] = " BARGAINBURG "

		self.names[19] = " GREAT FRONTIER "

		self.names[20] = " GREAT FRONTIER "

		self.names[21] = " GREAT FRONTIER "

		self.names[22] = " GREAT FRONTIER "

		self.names[23] = " GREAT FRONTIER "

		self.names[24] = " GREAT FRONTIER "

		self.names[25] = " WINDSWEPT BLUFF "

		self.names[26] = " STORMWALL PASS "

		self.names[27] = " STORMWALL PASS "

		self.names[28] = " STORMWALL PASS "

		self.names[29] = " STORMWALL PASS "

		self.names[30] = " STORMWALL PASS "

		self.names[31] = " STORMWALL PASS "

		self.names[32] = " CHAPEL PERILOUS "

		self.names[33] = " CHAPEL PERILOUS "

		self.names[34] = " CHAPEL PERILOUS "

		self.names[35] = " CHAPEL PERILOUS "

		self.names[36] = " BLUE RUIN "

		self.names[37] = " BLUE RUIN "

		self.names[38] = " BLUE RUIN "

		self.names[39] = " THE TOWER "

		self.names[40] = " THE TOWER "

		self.names[41] = " THE TOWER "

		self.names[42] = " THE TOWER "

	def blitme(self, screen):

		if self.blit_name:

			if self.blit_type:

				text = self.small_font.render(self.blit_name, True, (255, 255, 255))

			else:

				text = self.font.render(self.blit_name, True, (255, 255, 255))

			if self.blit_type:

				middle_screen = pygame.Surface(text.get_size(), pygame.SRCALPHA)

				middle_screen.fill((255, 255, 255, self.opacity))

				text.blit(middle_screen, (0, 0), special_flags = pygame.BLEND_RGBA_MULT)

				screen.blit(text, (0, screen.get_height() - text.get_height()))

			else:

				final_screen = pygame.Surface((text.get_width() + 100, text.get_height()), pygame.SRCALPHA)

				text_start, text_end = (final_screen.get_width() - text.get_width()) / 2, (final_screen.get_width() - text.get_width()) / 2 + text.get_width()

				final_screen.blit(text, ((text_start, 0)))

				pygame.draw.line(final_screen, (255, 255, 255), (0, final_screen.get_height() / 2), (text_start, final_screen.get_height() / 2), 1)

				pygame.draw.line(final_screen, (255, 255, 255), (text_end, final_screen.get_height() / 2), (final_screen.get_width(), final_screen.get_height() / 2), 1)

				middle_screen = pygame.Surface(final_screen.get_size(), pygame.SRCALPHA)

				middle_screen.fill((255, 255, 255, self.opacity))

				final_screen.blit(middle_screen, (0, 0), special_flags = pygame.BLEND_RGBA_MULT)

				screen.blit(final_screen, ((screen.get_width() - final_screen.get_width()) / 2, (screen.get_height() - final_screen.get_height()) / 2))

			self.opacity -= 1

			if self.opacity <= 0:

				self.active = False

				self.opacity = 255

				self.blit_type = None

				self.blit_name = None

	def play_audio(self):

		if not self.channel.get_busy() and self.active and not self.blit_type:

			self.channel.play(self.audio)

