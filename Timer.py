#!/usr/bin/env python
#
#
#
#

import pygame

class Timer:

	def __init__(self):

		pygame.init()

		self.start_time = None

	def start(self):

		self.start_time = pygame.time.get_ticks()

	def elapsed_time(self):

		return pygame.time.get_ticks() - self.start_time

	def end(self):

		self.start_time = None

