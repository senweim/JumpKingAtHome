#!/usr.bin/env python
#
#
#
#

import pygame
import collections
import os
import re
import sys

class Weathers:

	def __init__(self):

		self.width, self.height = int(os.environ.get("screen_width")), int(os.environ.get("screen_height"))

		self.wind_levels = [25, 26, 27, 28, 29, 30, 31]

		self.directory = "weather"

		self.rain_color = (101, 157, 191)

		self.snow_color = (100, 100, 100)

		self.weather = collections.defaultdict()

		self._load_images()

	def _load_weather(self, weather):

		frames = []

		for file in sorted(os.listdir(self.directory), key = lambda filename: int(re.search(r'\d+', filename).group())):

			if re.search(r"^{weather}\d+".format(weather = weather), file):

				frame = pygame.image.load(f"{self.directory}\\{file}")

				frames.append(frame)

		return frames

	def _load_images(self):

		for file in os.listdir(self.directory):
	
			name = re.search(r"(.*)mask(\d+)", file)

			if name:

				mask = self._load_mask(file)

				weather_frames = self._load_weather(name.group(1))

				if "snow" in name.group(1):

					color = self.snow_color

				elif "rain" in name.group(1):

					color = self.rain_color

				level = int(name.group(2)) - 1

				hasWind = level in self.wind_levels

				images = []

				for frame in weather_frames:

					image = pygame.Surface((self.width, self.height), pygame.SRCALPHA).convert()
					image.fill(color)
					image.set_colorkey(color, pygame.RLEACCEL)

					beta_image = pygame.Surface((self.width, self.height), pygame.SRCALPHA).convert()
					beta_image.fill(color)
					beta_image.set_colorkey((0, 0, 0), pygame.RLEACCEL)

					pygame.draw.polygon(beta_image, (0, 0, 0), mask.outline(), 0)


					for i in range(self.height // frame.get_height()):

						for j in range(self.width // frame.get_width()):

							image.blit(frame, (j * frame.get_width(), i * frame.get_height()))

					image.blit(beta_image, beta_image.get_rect())

					images.append(image)

				self.weather[level] = Weather(images, hasWind)

	def _load_mask(self, file):

		mask = pygame.image.load(f"{self.directory}\\{file}")

		mask = pygame.mask.from_surface(mask)

		return mask

class Weather:

	def __init__(self, images, wind):

		self.images = images

		self.hasWind = wind

		self.counter = 0

		self.interval = 6

	def blitme(self, screen, wind):

		if self.counter >= self.interval * len(self.images):

			self.counter = 0

		image = self.images[self.counter // self.interval]

		if self.hasWind:

			rect = wind

			if rect.x > image.get_width():

				rect.x -= rect.x // image.get_width() * rect.width

			if rect.x < -image.get_width():

				rect.x += rect.x // image.get_width() * rect.width

			if rect.colliderect(screen.get_rect()):
				screen.blit(image, rect)

			if rect.move(image.get_width(), 0).colliderect(screen.get_rect()):
				screen.blit(image, rect.move(image.get_width(), 0))

			if rect.move(-image.get_width(), 0).colliderect(screen.get_rect()):
				screen.blit(image, rect.move(-image.get_width(), 0))

		else:

			screen.blit(image, (0, 0))

		self.counter += 1



if __name__ == "__main__":


	pygame.init()

	mega_screen = pygame.display.set_mode((480, 360), pygame.SRCALPHA)

	alpha_screen = pygame.Surface((480, 360), pygame.SRCALPHA).convert()
	alpha_screen.set_colorkey((0, 0, 0), pygame.RLEACCEL)
	
	screen = pygame.Surface((480, 360), pygame.SRCALPHA).convert()
	screen.set_colorkey((0, 255, 0), pygame.RLEACCEL)

	mask = pygame.mask.from_surface(pygame.image.load("weather\\rainmask13.png"))

	beta_screen = pygame.Surface((480, 360), pygame.SRCALPHA).convert()
	beta_screen.set_colorkey((255, 0, 0), pygame.RLEACCEL)

	#print(mask.outline())

	clock = pygame.time.Clock()

	a = 0

	while True:

		a += 1

		if a > 3:

			a = 1

		clock.tick(5)

		mega_screen.fill((200, 200, 200))

		screen.fill((0, 0, 0))

		beta_screen.fill((0, 255, 0))

		wack = pygame.Surface((480, 360), pygame.SRCALPHA).convert()

		rain = pygame.image.load(f"weather\\light_rain{a}.png").convert_alpha()

		for event in pygame.event.get():

			if event.type == pygame.QUIT:

				sys.exit()

		for i in range(screen.get_height() // rain.get_height()):

			for j in range(screen.get_width() // rain.get_width()):

				screen.blit(rain, (rain.get_width() * j, rain.get_height() * i))

		pygame.draw.polygon(beta_screen, (255, 0, 0), mask.outline(), 0)

		screen.blit(beta_screen, (0, 0))

		alpha_screen.blit(screen, (0, 0))

		mega_screen.blit(alpha_screen, (0, 0))

		pygame.display.flip()