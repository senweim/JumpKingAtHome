#!/usr/bin/env python
#
#
#
#

import pygame
import math
import os
import re

class Start:

	def __init__(self, screen, menus):

		self.screen = screen

		self.channels = [pygame.mixer.Channel(0), pygame.mixer.Channel(15)]

		self.menus = menus

		self.images = self._load_images()

		self.audio = self._load_audio()

		# Animation

		self.opacity = 255

		self.opacity_fadespeed = 15

		self.text = Text("LEGEND HAS IT THERE IS A BABE AT THE TOP...")

		self.title_logo = Title(self.images)

		self.Nexile_Logo_Counter = 500

		self.complete = False

	def _load_audio(self):

		audio = {}

		for audio_name in os.listdir("audio\\start"):

			audio[re.match(r"[^.]+", audio_name).group()] = pygame.mixer.Sound(f"audio\\start\\{audio_name}")

		return audio		

	def _load_images(self):

		images = {}

		for image_name in os.listdir("images\\logos"):

			images[re.match(r"[^.]+", image_name).group()] = pygame.image.load(f"images\\logos\\{image_name}").convert_alpha()

		return images

	def blit_nexile_logo(self):

		if self.Nexile_Logo_Counter > 100:

			self.screen.fill((255, 255, 255))

			self.screen.blit(self.images["JK_Nexile_Logo"], ((self.screen.get_width() - self.images["JK_Nexile_Logo"].get_width()) / 2, (self.screen.get_height() - self.images["JK_Nexile_Logo"].get_height()) / 2))

		self.Nexile_Logo_Counter -= 1

	def blitme(self):

		if not os.environ["start"]:

			if self.Nexile_Logo_Counter:

				self.blit_nexile_logo()

			else:

				self.title_logo.blitme(self.screen)

		else:

			self.title_logo.blitme(self.screen)

		if os.environ["active"]:

			if not self.title_logo.fadecomplete:

				self.title_logo.blitme(self.screen)

			elif self.title_logo.fadecomplete and not self.text.fadecomplete:

				self.text.blitme(self.screen)

	def update(self):
		if not os.environ["start"]:

			if self.Nexile_Logo_Counter:

				pass

			elif self.title_logo.y != self.title_logo.end and not self.title_logo.complete:

				if not self.channels[0].get_busy():

					self.channels[0].play(self.audio["menu_intro"])

				self.title_logo.move_up()

				self.title_logo.brighten()

			else:

				if not self.title_logo.complete:

					self.channels[1].play(self.audio["title_hit"])

				if not self.channels[0].get_busy():

					self.channels[0].play(self.audio["menu_loop"])

				self.title_logo.complete = True

				self.title_logo.shake()

				self.menus.current_menu = self.menus.menus["Press_Start"]

				self.menus.current_menu.active = True

		if os.environ["active"]:
			self.title_logo.fade()

			for channel in self.channels:
				channel.stop()

			if self.title_logo.fadecomplete and not self.text.complete:

				self.text.brighten()

			elif self.text.complete and not self.text.fadecomplete:

				self.text.fade()

			elif self.text.fadecomplete and not self.complete:

				self.fade()

			elif self.complete:
				self.reset()
				os.environ["gaming"] = "1"
				os.environ["pause"] = ""

	def fade(self):

		if self.opacity > 0:

			self.opacity -= self.opacity_fadespeed

		elif self.opacity == 0:

			self.complete = True

	def reset(self):

		self.opacity = 255

		self.Nexile_Logo_Counter = 500

		self.complete = False

		self.title_logo.reset()

		self.text.reset()

class Title:

	def __init__(self, images):

		self.images = images

		self.shake_counter, self.shake_interval, self.shake_length = 21, 3, 5

		self.start, self.end = round(int(os.environ.get("screen_width")) / 4), round(int(os.environ.get("screen_height")) / 8)

		self.opacity = 0

		self.opacity_fadespeed = 5

		self.speed = 0.5

		self.width, self.height = self.images["title_logo"].get_size()

		self.x, self.y = round((int(os.environ.get("screen_width")) - self.width) / 2), self.start

		self.complete = False

		self.fadecomplete = False

		self.inititated = False

	def reset(self):

		self.shake_counter, self.shake_interval, self.shake_length = 21, 3, 5

		self.start, self.end = round(int(os.environ.get("screen_width")) / 4), round(int(os.environ.get("screen_height")) / 8)

		self.opacity = 0

		self.opacity_fadespeed = 5

		self.speed = 0.5

		self.width, self.height = self.images["title_logo"].get_size()

		self.x, self.y = round((int(os.environ.get("screen_width")) - self.width) / 2), self.start

		self.complete = False

		self.fadecomplete = False

		self.inititated = False

	def brighten(self):

		self.opacity = int(255 * (1 - (self.y - self.end) / (self.start - self.end)))

	def fade(self):

		if self.opacity > 0:

			self.opacity -= self.opacity_fadespeed

		else:

			self.fadecomplete = True

	def shake(self):

		if self.shake_counter:

			if not self.shake_counter // self.shake_interval % 2:

				self.y = self.end - self.shake_length

			elif self.shake_counter // self.shake_interval % 2:

				self.y = self.end + self.shake_length

			self.shake_counter -= 1

	def blitme(self, screen):

		image = self.images["title_logo"].copy()

		middle_screen = pygame.Surface(image.get_size(), pygame.SRCALPHA)

		middle_screen.fill((255, 255, 255, self.opacity))

		image.blit(middle_screen, (0, 0), special_flags = pygame.BLEND_RGBA_MULT)

		screen.blit(image, (int(self.x), int(self.y)))			

	def move_up(self):

		self.y -= self.speed

class Text(Title):

	def __init__(self, text):

		self.font = pygame.font.Font("Fonts\\ttf_pixolde_bold.ttf", 20)

		self.text = self._fold(text)

		self.opacity = 0

		self.opacity_fadespeed = 1

		self.complete = False

		self.fadecomplete = False

	def reset(self):

		self.opacity = 0

		self.opacity_fadespeed = 1

		self.complete = False

		self.fadecomplete = False	

	def _fold(self, text):

		t = []

		for index, line in enumerate(map(lambda x: x[0], re.findall(r"(([^ .,!?]+[ .,!?]*){0,6})", text))):

			t.append(self.font.render(line, True, (255, 255, 255)))

		return t

	def blitme(self, screen):

		text_screen = pygame.Surface((max([text.get_width() for text in self.text]), sum([text.get_height() for text in self.text])), pygame.SRCALPHA)

		middle_screen = pygame.Surface(text_screen.get_size(), pygame.SRCALPHA)

		middle_screen.fill((255, 255, 255, self.opacity))

		for index, text in enumerate(self.text):

			text_screen.blit(text, ((text_screen.get_width() - text.get_width()) / 2, (index)*text.get_height()))

		text_screen.blit(middle_screen, (0, 0), special_flags = pygame.BLEND_RGBA_MULT)

		screen.blit(text_screen, ((screen.get_width() - text_screen.get_width()) / 2, (screen.get_height() - text_screen.get_height()) / 2))	

	def brighten(self):

		if self.opacity != 255:

			self.opacity += self.opacity_fadespeed

		elif self.opacity == 255:

			self.complete = True

