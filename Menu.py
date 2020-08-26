#!/usr/bin/env python
#
#
#
#

import pygame
import os
import sys
import re
import pickle
from spritesheet import SpriteSheet

class Menus:

	def __init__(self, screen, levels, king):

		self.screen = screen

		self.directory = "gui"

		self.levels = levels

		self.king = king

		self.font = pygame.font.Font("Fonts\\ttf_pixolde_bold.ttf", 16)

		self.current_menu = None

		self.channels = [pygame.mixer.Channel(17), pygame.mixer.Channel(18)]

		self.audio = self._load_audio("Audio\\gui_sfx")

		self.images = self._load_images(self.directory)

		self.buttons = self._load_buttons()

		self.menus = self._load_menus()

	def check_events(self, event):

		if event.key == pygame.K_ESCAPE:

			if os.environ["gaming"]:

				if not os.environ["pause"]:

					os.environ["pause"] = "1"
					self.current_menu = self.menus["Pause_Menu"]
					self.menus["Pause_Menu"].open()

				elif os.environ["pause"]:

					os.environ["pause"] = ""
					self.current_menu = None
					self.menus["Pause_Menu"].close()

		if self.current_menu:

			if event.key == pygame.K_SPACE:

				self.current_menu.activate()

			if event.key == pygame.K_UP:

				if self.current_menu.current_index:

					self.current_menu.current_index -= 1

			if event.key == pygame.K_DOWN:

				if self.current_menu.current_index < len(self.current_menu.buttons) - 1:

					self.current_menu.current_index += 1

	def update(self):

		self.current_menu.update()

	def _load_buttons(self):

		buttons = {}

		buttons["Back_Button"] = Button(self.font, self.images["back"], self.back)

		buttons["Save_Exit_Button"] = Button(self.font, self.font.render("SAVE & EXIT", True, (255, 255, 255)), self.save_exit)

		buttons["Press_Start"] = Button(self.font, self.font.render("PRESS SPACE", True, (255, 255, 255)), self.press_start)

		buttons["New_Game"] = Button(self.font, self.font.render("NEW GAME", True, (255, 255, 255)), self.new_game)

		buttons["Continue_Game"] = Button(self.font, self.font.render("CONTINUE", True, (255, 255, 255)), self.load_game)

		buttons["Exit"] = Button(self.font, self.font.render("EXIT", True, (255, 255, 255)), self.exit)

		return buttons

	def _load_menus(self):

		menus = {}

		menus["Pause_Menu"] = Menu(None, 300, 40, 128, 128, self.images, self.audio, self.buttons["Save_Exit_Button"], self.buttons["Back_Button"])

		menus["Start_Menu"] = Menu(None, 20, 150, 128, 128, self.images, self.audio, self.buttons["New_Game"], self.buttons["Exit"])

		if "save.dat" in os.listdir("Saves"):

			menus["Start_Menu"].buttons.insert(0, self.buttons["Continue_Game"])

		menus["Press_Start"] = Blinker_Menu(None, (self.screen.get_width() - self.buttons["Press_Start"].text.get_width()) / 2, 5 * self.screen.get_height() / 7, self.buttons["Press_Start"].text.get_width(), self.buttons["Press_Start"].text.get_height(), self.images, self.audio, self.buttons["Press_Start"])

		return menus

	def _load_audio(self, file):

		audios = {}

		for audio_name in os.listdir(file):

			audios[re.match(r"[^.]+", audio_name).group()] = pygame.mixer.Sound(f"{file}\\{audio_name}")

		return audios
	
	def _load_images(self, file):

		images = {}

		for image_name in os.listdir(file):

			if image_name == "frame.png":

				image = SpriteSheet(f"{file}\\{image_name}")

				image_names = ["topleft", "top", "topright", "left", "center", "right", "bottomleft", "bottom", "bottomright"]

				images["frame"] = dict(zip(image_names, image.load_grid((0, 0, 16, 16), 3, 3, -1)))

			else:

				images[re.match(r"[^.]+", image_name).group()] = pygame.image.load(f"{file}\\{image_name}").convert_alpha()

		return images

	def exit(self):

		self.channels[0].play(self.audio["selectA"])

		sys.exit()

	def blitme(self):

		for menu in self.menus.values():

			menu.blitme(self.screen)

	def save_exit(self):

		self.channels[0].play(self.audio["selectA"])

		with open("Saves\\save.dat", "wb") as file:

			pickle.dump(self.game_state(), file)

		os.environ["start"] = ""

		os.environ["active"] = ""

		os.environ["gaming"] = ""

		os.environ["pause"] = "1"

		self.current_menu.close()

		self.current_menu = None

		self.menus = self._load_menus()

		pygame.mixer.stop()

	def new_game(self):

		self.channels[0].play(self.audio["selectA"])

		self.channels[1].play(self.audio["opening_theme"])

		with open("Saves\\save.dat", "wb") as file:

			pickle.dump(self.game_state(), file)

		os.environ["active"] = "1"

		self.current_menu.close()

		self.current_menu = None	

	def back(self):

		self.channels[0].play(self.audio["selectA"])

		if self.current_menu:

			self.current_menu.close()

			self.current_menu = self.current_menu.parent

		if not self.current_menu:

			os.environ["pause"] = ""

	def load_game(self):

		self.channels[0].play(self.audio["selectA"])

		self.channels[1].play(self.audio["opening_theme"])

		with open("Saves\\save.dat", "rb") as file:

			state = pickle.load(file)

			self.king.rect_x = state["KING"]["x"]
			self.king.rect_y = state["KING"]["y"]
			self.king.speed = state["KING"]["speed"]
			self.king.angle = state["KING"]["angle"]
			self.king.direction = state["KING"]["direction"]
			self.king.isWalk = state["KING"]["isWalk"]
			self.king.isCrouch = state["KING"]["isCrouch"]
			self.king.isFalling = state["KING"]["isFalling"]
			self.king.isContact = state["KING"]["isContact"]
			self.king.isSplat = state["KING"]["isSplat"]
			self.king.isDance = state["KING"]["isDance"]
			self.king.isSnatch = state["KING"]["isSnatch"]
			self.king.isHoldingUpHands = state["KING"]["isHoldingUpHands"]
			self.king.isHoldingBabe = state["KING"]["isHoldingBabe"]
			self.king.isAdmiring = state["KING"]["isAdmiring"]
			self.king.isWearingCrown = state["KING"]["isWearingCrown"]
			self.king.collided = state["KING"]["collided"]
			self.king.jumpParticle = state["KING"]["jumpParticle"]
			self.king.lastCollision = state["KING"]["lastCollision"]
			self.king.collideTop = state["KING"]["collideTop"]
			self.king.collideRight = state["KING"]["collideRight"]
			self.king.collideLeft = state["KING"]["collideLeft"]
			self.king.collideBottom = state["KING"]["collideBottom"]
			self.king.collideRamp = state["KING"]["collideRamp"]
			self.king.isJump = state["KING"]["isJump"]
			self.king.isLanded = state["KING"]["isLanded"]

			self.levels.current_level = state["LEVELS"]["current_level"]
			self.levels.wind.x = state["LEVELS"]["wind_x"]
			self.levels.wind_var = state["LEVELS"]["wind_var"]
			self.levels.shake_var = state["LEVELS"]["shake_var"]

			for flyer in self.levels.flyers:

				self.levels.flyers[flyer].x = state["LEVELS"]["flyer_x"][flyer]
				self.levels.flyers[flyer].y = state["LEVELS"]["flyer_y"][flyer]

			for scrollers in self.levels.scrollers:

				for scroller in range(len(self.levels.scrollers[scrollers])):

					self.levels.scrollers[scrollers][scroller].x = state["LEVELS"]["scroller_x"][scrollers][scroller]
					self.levels.scrollers[scrollers][scroller].y = state["LEVELS"]["scroller_y"][scrollers][scroller]

		self.king._update_sprites()

		os.environ["active"] = "1"

		self.current_menu.close()

		self.current_menu = None

	def game_state(self):

		state = {	"KING"	 : {	"x" : self.king.rect_x,
									"y" : self.king.rect_y,
									"speed" : self.king.speed,
									"angle" : self.king.angle,
									"direction" : self.king.direction,
									"isWalk" : self.king.isWalk,
									"isCrouch" : self.king.isCrouch,
									"isFalling" : self.king.isFalling,
									"isContact" : self.king.isContact,
									"isSplat" :	self.king.isSplat,
									"isDance" :	self.king.isDance,
									"isLookUp" : self.king.isLookUp,
									"isSnatch" : self.king.isSnatch,
									"isHoldingUpHands" : self.king.isHoldingUpHands,
									"isHoldingBabe" : self.king.isHoldingBabe,
									"isAdmiring" : self.king.isAdmiring,
									"isWearingCrown" : self.king.isWearingCrown,
									"collided" : self.king.collided,
									"jumpParticle" : self.king.jumpParticle,
									"lastCollision" : self.king.lastCollision,
									"collideTop" : self.king.collideTop,
									"collideRight" : self.king.collideRight,
									"collideLeft" : self.king.collideLeft,
									"collideBottom" : self.king.collideBottom,
									"collideRamp" : self.king.collideRamp,
									"isJump" : self.king.isJump,
									"isLanded" : self.king.isLanded									
																},

					"LEVELS" : {
									"current_level" : self.levels.current_level,
									"wind_x" : self.levels.wind.x,
									"wind_var" : self.levels.wind.wind_var,
									"shake_var" : self.levels.shake_var,
									"flyer_x" : {flyer : self.levels.flyers[flyer].x for flyer in self.levels.flyers},
									"flyer_y" : {flyer : self.levels.flyers[flyer].y for flyer in self.levels.flyers},
									"scroller_x" : {scrollers : [scroller.x for scroller in self.levels.scrollers[scrollers]] for scrollers in self.levels.scrollers},
									"scroller_y" : {scrollers : [scroller.y for scroller in self.levels.scrollers[scrollers]] for scrollers in self.levels.scrollers}
																}
																	}

		return state

	def press_start(self):

		os.environ["start"] = "1"

		self.current_menu.reset()

		self.current_menu.active = False
		
		self.current_menu = self.menus["Start_Menu"]

		self.current_menu.active = True

class Menu:

	def __init__(self, parent, x, y, width, height, images, audio, *buttons):

		self.parent = parent

		self.x, self.y, self.width, self.height = x, y, width, height

		self.images = images

		self.audio = audio

		self.channels = [pygame.mixer.Channel(17), pygame.mixer.Channel(18)]

		self.buttons = list(buttons)

		self.current_index = 0

		self.blit_counter = 0

		self.active = False

	@property
	def current_button(self):

		return self.buttons[self.current_index]

	def close(self):

		self.active = False

		self.current_index = 0

	def open(self):

		self.active = True

		self.channels[0].play(self.audio["menu_open"])

	def blitme(self, screen):

		if self.active:

			frame = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

			width, height = self.images["frame"]["top"].get_size()

			# Corners

			for x in range(0, (self.width // width) * width, width):

				for y in range(0, (self.height // height) * height, height):

					if x == 0:

						if y == 0:

							frame.blit(self.images["frame"]["topleft"], (x, y))

						elif y == self.height - height:

							frame.blit(self.images["frame"]["bottomleft"], (x, y))

						else:

							frame.blit(self.images["frame"]["left"], (x, y))

					elif x == self.width - width:

						if y == 0:

							frame.blit(self.images["frame"]["topright"], (x, y))

						elif y == self.height - height:

							frame.blit(self.images["frame"]["bottomright"], (x, y))

						else:

							frame.blit(self.images["frame"]["right"], (x, y))

					elif y == 0:

						frame.blit(self.images["frame"]["top"], (x, y))

					elif y == self.height - height:

						frame.blit(self.images["frame"]["bottom"], (x, y))

					else:

						frame.blit(self.images["frame"]["center"], (x, y))

				if self.blit_counter > 10:

					for index, button in enumerate(self.buttons):

						frame.blit(button.text, (20, (index + 1) * 16))

						if button == self.current_button:

							frame.blit(self.images["cursor"], (0, (index + 1) * 16))

				self.blit_counter += 1

			screen.blit(frame, (self.x, self.y))

		else:

			self.blit_counter = 0

	def update(self):
		pass

	def activate(self):

		self.current_button.activate()

class Blinker_Menu(Menu):

	def __init__(self, parent, x, y, width, height, images, audio, button):

		super().__init__(parent, x, y, width, height, images, audio, None)

		self.button = button

		self.blinking = False

		self.blink_counter = 0

		self.blit_counter = 0

		self.blit_long_interval = 30

		self.blit_interval = 5

		self.blink_length = 15

	def update(self):

		if self.blinking and self.blink_counter >= self.blink_length:

			self.button.activate()

	def blitme(self, screen):

		if self.active:

			if self.blinking:

				if self.blit_counter // self.blit_interval % 2:

					screen.blit(self.button.text, (self.x, self.y))

					self.blink_counter += 1

			else:

				if self.blit_counter // self.blit_long_interval % 2:

					screen.blit(self.button.text, (self.x, self.y))

			self.blit_counter += 1

	def reset(self):

		self.blinking = False

		self.blink_counter = 0

		self.blit_counter = 0

		self.blit_long_interval = 30

		self.blit_interval = 5

		self.blink_length = 7		

	def activate(self):

		self.channels[0].play(self.audio["press_start"])
		self.blinking = True

class Button:

	def __init__(self, font, text, function):

		self.text = text

		self.function = function

	def activate(self):

		return self.function()






