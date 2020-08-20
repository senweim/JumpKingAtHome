#!/usr/bin/env python
#
#
#
#

class Camera:

	def __init__(self, screen):

		self.screen = screen
		self.screen_width = screen.get_width()
		self.screen_height = screen.get_height()

		self.level = 0

		
	@property
	def Y(self):

		return self.level * self.screen_height
	


	