#!/usr/bin/env python
#
#
#
#

import pygame

class Timer:

	def __init__(self):

		self.start_time = None

	def start(self):

		self.start_time = pygame.time.get_ticks()

	def elapsed_time(self):

		x = pygame.time.get_ticks() - self.start_time

		self.start_time = pygame.time.get_ticks()

		return x

	def end(self):

		self.start_time = None

