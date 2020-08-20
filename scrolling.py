#!/usr/bin/env python
#
#
#
#

import pygame
import collections
import os
from spritesheet import SpriteSheet

class Scrollers:

	def __init__(self):

		self.images = collections.defaultdict()

		self.scrollers = collections.defaultdict()

		self._load_images()

	def _load_images(self):

		for file in os.listdir("Scrolling"):

			if "bird" in file:

				self.images[file] = Birds().load_image(file)

			else:

				self.images[file] = Cloud().load_image(file)

		self.scrollers[3] = [Cloud(-40, 50, 0.05, self.images["4_clouds.png"], "bg")]

		self.scrollers[4] = [Cloud(-40, 70, 0.05, self.images["6_clouds.png"], "bg")]

		self.scrollers[5] = [Cloud(20, 200, 0.05, self.images["6_clouds.png"], "bg")]

		self.scrollers[13] = [Cloud(-30, 10, 0.05, self.images["14_clouds_bg.png"], "bg"), 
							Cloud(-30, 50, 0.10, self.images["14_clouds_mg.png"], "bg"), 
							Cloud(-30, 150, 0.25, self.images["14_clouds_fg.png"], "bg")]

		self.scrollers[14] = [Cloud(-30, 10, 0.25, self.images["mist_clouds1.png"], "fg"), 
							Cloud(30, 100, 0.5, self.images["mist_clouds2.png"], "fg"), Cloud(70, 250, 0.4, self.images["mist_clouds3.png"], "fg"),
							Birds(470, 40, -0.5, self.images["bird_cloud.png"], "bg"), Birds(50, 200, 0.1, self.images["bird_cloud.png"], "bg")]

		self.scrollers[15]  = [Cloud(-30, 10, 0.25, self.images["mist_clouds1.png"], "fg"), Cloud(30, 100, 0.5, self.images["mist_clouds2.png"], "fg"), 
							Cloud(70, 250, 0.4, self.images["mist_clouds3.png"], "fg"),
							Birds(470, 300, -0.5, self.images["bird_cloud.png"], "bg")]

		self.scrollers[16] = [Cloud(-30, 10, 0.25, self.images["mist_clouds1.png"], "fg"), Cloud(30, 100, 0.5, self.images["mist_clouds2.png"], "fg"), 
							Cloud(70, 250, 0.4, self.images["mist_clouds3.png"], "fg"),
							Birds(470, 200, -0.5, self.images["bird_cloud.png"], "bg"), 
							Birds(50, 50, 0.1, self.images["bird_cloud.png"], "bg")]

		self.scrollers[17]  = [Cloud(-30, 10, 0.25, self.images["mist_clouds1.png"], "fg"), Cloud(30, 100, 0.5, self.images["mist_clouds2.png"], "fg"), 
							Cloud(70, 250, 0.4, self.images["mist_clouds3.png"], "fg"),
							Birds(470, 10, 0.5, self.images["bird_cloud.png"], "bg")]

		self.scrollers[18]  = [Cloud(-30, 10, 0.25, self.images["mist_clouds1.png"], "fg"), Cloud(30, 100, 0.5, self.images["mist_clouds2.png"], "fg"),
							Cloud(70, 250, 0.4, self.images["mist_clouds3.png"], "fg"),
							Birds(470, 200, 0.5, self.images["bird_cloud.png"], "bg")]

		self.scrollers[19] = [Cloud(-30, 20, 0.1, self.images["clouds_vakttorn1.png"], "bg"), Cloud(-10, 160, 0.05, self.images["clouds_vakttorn2.png"], "bg")]
		self.scrollers[19] = [Cloud(-30, 20, 0.1, self.images["clouds_vakttorn2.png"], "bg"), Cloud(-10, 200, 0.05, self.images["clouds_vakttorn1.png"], "bg")]
		self.scrollers[20] = [Cloud(-30, 100, 0.1,self.images["clouds_vakttorn2.png"], "bg"), Cloud(90, 160, 0.05, self.images["clouds_vakttorn1.png"], "bg")]
		self.scrollers[21] = [Cloud(-30, 20, 0.1, self.images["clouds_vakttorn1.png"], "bg"), Cloud(-10, 160, 0.05, self.images["clouds_vakttorn2.png"], "bg")]
		self.scrollers[22] = [Cloud(-30, 20, 0.1, self.images["clouds_vakttorn_dark2.png"],"bg"), Cloud(-10, 160, 0.05, self.images["clouds_vakttorn1.png"], "bg")]
		self.scrollers[23] = [Cloud(-30, 20, 0.1, self.images["clouds_vakttorn_dark1.png"],"bg"), Cloud(-10, 160, 0.05, self.images["clouds_vakttorn_dark2.png"], "bg")]
		self.scrollers[24] = [Cloud(-30, 20, 0.1, self.images["clouds_vakttorn_dark1.png"],"bg"), Cloud(-10, 160, 0.05, self.images["clouds_vakttorn_dark2.png"], "bg")]

		self.scrollers[39] = [Cloud(0, 0, 0.1, self.images["40_clouds.png"],"bg")]
		self.scrollers[40] = [Cloud(0, 60, 0.1, self.images["41_clouds.png"],"bg")]
		self.scrollers[41] = [Cloud(0, 224, 0.1, self.images["42_clouds1.png"],"bg"), Cloud(0, 100, 0.1, self.images["42_clouds2.png"],"bg")]


class Cloud:

	def __init__(self, x = 0, y = 0, speed = None, image = None, layer = None):

		self.directory = "Scrolling"

		self.scale = int(os.environ.get("resolution"))

		self.layer = layer

		self.x, self.y = x * self.scale, y * self.scale

		self.speed = speed

		self.image = image

	def blitme(self, screen, layer):

		if layer == self.layer:

			screen.blit(self.image, (self.x, self.y))#, special_flags = pygame.BLEND_RGB_MAX)
			screen.blit(self.image, (self.x - self.image.get_width(), self.y))#, special_flags = pygame.BLEND_RGB_MAX)
			screen.blit(self.image, (self.x + self.image.get_width(), self.y))#, special_flags = pygame.BLEND_RGB_MAX)

			self.x += self.speed * self.scale

			if self.x > screen.get_width():

				self.x = self.x - self.image.get_width()

			if self.x < 0 - self.image.get_width():

				self.x = self.x + self.image.get_width()

	def load_image(self, file):

		image = pygame.image.load(f"{self.directory}\\{file}").convert_alpha()

		image = pygame.transform.scale(image, (image.get_width() * self.scale, image.get_height() * self.scale))

		return image

class Birds:

	def __init__(self, x = 0, y = 0, speed = 0, images = None, layer = None):

		self.directory = "Scrolling"

		self.scale = int(os.environ.get("resolution"))

		self.layer = layer

		self.speed = speed

		self.start_rect = (0, 0, 128, 96)

		self.x, self.y = x * self.scale, y * self.scale

		self.blit_counter = 0

		self.images = images

	def blitme(self, screen, layer):

		if layer == self.layer:

			if self.blit_counter == 48:

				self.blit_counter = 0

			screen.blit(self.images[self.blit_counter//6], (self.x, self.y))

			self.blit_counter += 1

			self.x += self.speed * self.scale

			if self.x > screen.get_width():

				self.x = self.x - self.images[0].get_width()

			if self.x < 0 - self.images[0].get_width():
				
				self.x = screen.get_width()

	def load_image(self, file):

		spritesheet = SpriteSheet(f"{self.directory}\\{file}")

		images = spritesheet.load_grid(self.start_rect, 2, 4, -1)

		return images