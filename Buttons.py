#!/usr/bin/env python
#
#
#
#

import pygame

class Buttons:

	def __init__(self, font):
		

	def _load_buttons(self):

		buttons = {}

		buttons["Back_Button"] = Button(self.font, self.images["back"], self.back)

		buttons["Save_Exit_Button"] = Button(self.font, self.font.render("Save & Exit", True, (255, 255, 255)), self.save_exit)

		return buttons

class Button:

	def __init__(self, font, text, function):

		self.text = text

		self.function = function

	def activate(self):

		return self.function()

