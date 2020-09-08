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

		self.channels = [pygame.mixer.Channel(13), pygame.mixer.Channel(14)]

		self.audio = self._load_audio("Audio\\gui_sfx")

		self.images = self._load_images(self.directory)

		self.buttons = self._load_buttons()

		self.menus = self._load_menus()

	def update(self):

		self.current_menu.update()

		self.menus["Stat_Menu1"].update()

		self.menus["Stat_Menu2"].update()

	def check_events(self, event):

		if event.key == pygame.K_ESCAPE:

			if os.environ["gaming"]:

				if not os.environ["pause"]:

					os.environ["pause"] = "1"
					self.current_menu = self.menus["Pause_Menu"]
					self.king.timer.end()
					self.menus["Pause_Menu"].open()
					self.menus["Stat_Menu2"].open()

				elif os.environ["pause"]:

					os.environ["pause"] = ""
					self.current_menu = None
					self.close_menus()

		if self.current_menu:

			if event.key == pygame.K_SPACE:

				if not isinstance(self.current_menu.current_button, Slider) or not isinstance(self.current_menu.current_button, Number_Slider):

					self.current_menu.activate("space")

			if event.key == pygame.K_LEFT:

				if isinstance(self.current_menu.current_button, Slider) or isinstance(self.current_menu.current_button, Number_Slider):

					self.current_menu.activate("left")

			if event.key == pygame.K_RIGHT:

				if isinstance(self.current_menu.current_button, Slider) or isinstance(self.current_menu.current_button, Number_Slider):

					self.current_menu.activate("right")

			if event.key == pygame.K_UP:

				if isinstance(self.current_menu, Menu):

					if self.current_menu.current_index:

						self.current_menu.current_index -= 1

			if event.key == pygame.K_DOWN:

				if isinstance(self.current_menu, Menu):

					if self.current_menu.current_index < len(self.current_menu.buttons) - 1:

						self.current_menu.current_index += 1

	def _load_buttons(self):

		buttons = {}

		buttons["Back_Button"] = Button(self.font, self.images["back"], self.back)

		buttons["Save_Exit_Button"] = Button(self.font, self.font.render("SAVE & EXIT", True, (255, 255, 255)), self.pause_save_exit)

		buttons["Press_Start"] = Button(self.font, self.font.render("PRESS SPACE", True, (255, 255, 255)), self.press_start)

		buttons["New_Game"] = Button(self.font, self.font.render("NEW GAME", True, (255, 255, 255)), self.start_new_game)

		buttons["New_Game_Yes"] = Button(self.font, self.font.render("YES", True, (255, 255, 255)), self.new_game)

		buttons["New_Game_No"] = Button(self.font, self.font.render("NO", True, (255, 255, 255)), self.back)

		buttons["Save_Exit_No"] = Button(self.font, self.font.render("NO", True, (255, 255, 255)), self.back)

		buttons["Save_Exit_Yes"] = Button(self.font, self.font.render("YES", True, (255, 255, 255)), self.save_exit)

		buttons["Continue_Game"] = Button(self.font, self.font.render("CONTINUE", True, (255, 255, 255)), self.load_game)

		buttons["Pause_Options"] = Button(self.font, self.font.render("OPTIONS", True, (255, 255, 255)), self.pause_options)

		buttons["Start_Options"] = Button(self.font, self.font.render("OPTIONS", True, (255, 255, 255)), self.start_options)

		buttons["Pause_Options_Graphics"] = Button(self.font, self.font.render("GRAPHICS", True, (255, 255, 255)), self.pause_options_graphics)

		buttons["Pause_Options_Audio"] = Button(self.font, self.font.render("AUDIO", True, (255, 255, 255)), self.pause_options_audio)

		buttons["Start_Options_Graphics"] = Button(self.font, self.font.render("GRAPHICS", True, (255, 255, 255)), self.start_options_graphics)

		buttons["Start_Options_Audio"] = Button(self.font, self.font.render("AUDIO", True, (255, 255, 255)), self.start_options_audio)

		buttons["Audio_Slider"] = Slider(self.images["slider"], "volume", self.change_volume)

		buttons["Music_Checkbox"] = CheckBox(self.font, self.font.render("MUSIC", True, (255, 255, 255)), self.images["checkbox"], "music", self.change_music)

		buttons["Ambience_Checkbox"] = CheckBox(self.font, self.font.render("AMBIENCE", True, (255, 255, 255)), self.images["checkbox"], "ambience", self.change_ambience)

		buttons["Sfx_Checkbox"] = CheckBox(self.font, self.font.render("SFX", True, (255, 255, 255)), self.images["checkbox"], "sfx", self.change_sfx)

		buttons["Hitbox_Checkbox"] = CheckBox(self.font, self.font.render("HITBOXES", True, (255, 255, 255)), self.images["checkbox"], "hitboxes", self.change_hitboxes)

		buttons["Graphics_Slider"] = Number_Slider(self.font, self.images["arrows"], "window_scale", self.change_windowscale)

		buttons["Exit"] = Button(self.font, self.font.render("EXIT", True, (255, 255, 255)), self.exit)

		return buttons

	def _load_menus(self):

		menus = {}

		menus["Stat_Menu1"] = Stat_Menu(None, None, 240, 160, self.images, self.audio, Button(self.font, None, None), Button(self.font, None, None), Button(self.font, None, None), Button(self.font, None, None))

		menus["Stat_Menu2"] = Stat_Menu(None, None, 20, 40, self.images, self.audio, Button(self.font, None, None), Button(self.font, None, None), Button(self.font, None, None), Button(self.font, None, None))

		menus["Pause_Menu"] = Menu(None, None, 300, 40, self.images, self.audio, self.buttons["Save_Exit_Button"], self.buttons["Pause_Options"], self.buttons["Back_Button"])

		menus["Start_Menu"] = Menu(None, None, 20, 160, self.images, self.audio, self.buttons["New_Game"], self.buttons["Start_Options"], self.buttons["Exit"])

		menus["New_Game"] = Menu(menus["Start_Menu"], self.font.render("ARE YOU SURE?", True, (155, 0, 0)), menus["Start_Menu"].x + 40, menus["Start_Menu"].y, self.images, self.audio, self.buttons["New_Game_No"], self.buttons["New_Game_Yes"])

		menus["Save_Exit"] = Menu(menus["Pause_Menu"], self.font.render("ARE YOU SURE?", True, (155, 0, 0)), menus["Pause_Menu"].x - 40, menus["Pause_Menu"].y, self.images, self.audio, self.buttons["Save_Exit_No"], self.buttons["Save_Exit_Yes"])

		menus["Pause_Options"] = Menu(menus["Pause_Menu"], None, menus["Pause_Menu"].x - 40, menus["Pause_Menu"].y, self.images, self.audio, self.buttons["Pause_Options_Graphics"], self.buttons["Pause_Options_Audio"], self.buttons["Back_Button"])

		menus["Start_Options"] = Menu(menus["Start_Menu"], None, menus["Start_Menu"].x + 40, menus["Start_Menu"].y, self.images, self.audio, self.buttons["Start_Options_Graphics"], self.buttons["Start_Options_Audio"], self.buttons["Back_Button"])

		menus["Pause_Options_Graphics"] = Menu(menus["Pause_Options"], None, menus["Pause_Options"].x - 40, menus["Pause_Options"].y, self.images, self.audio, self.buttons["Graphics_Slider"], self.buttons["Hitbox_Checkbox"], self.buttons["Back_Button"])

		menus["Start_Options_Graphics"] = Menu(menus["Start_Options"], None, menus["Start_Options"].x + 40, menus["Start_Options"].y, self.images, self.audio, self.buttons["Graphics_Slider"], self.buttons["Hitbox_Checkbox"], self.buttons["Back_Button"])
		
		menus["Pause_Options_Audio"] = Menu(menus["Pause_Options"], None, menus["Pause_Options"].x - 40, menus["Pause_Options"].y, self.images, self.audio, self.buttons["Audio_Slider"], self.buttons["Music_Checkbox"], self.buttons["Ambience_Checkbox"], self.buttons["Sfx_Checkbox"], self.buttons["Back_Button"])

		menus["Start_Options_Audio"] = Menu(menus["Start_Options"], None, menus["Start_Options"].x + 40, menus["Start_Options"].y, self.images, self.audio, self.buttons["Audio_Slider"], self.buttons["Music_Checkbox"], self.buttons["Ambience_Checkbox"], self.buttons["Sfx_Checkbox"], self.buttons["Back_Button"])

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

			elif image_name == "slider.png":

				image = SpriteSheet(f"{file}\\{image_name}")

				image_names = ["left", "line", "right", "slider"]

				images["slider"] = dict(zip(image_names, image.load_strip((0, 0, 8, 8), 4, -1)))

			elif image_name == "checkbox.png":

				image = SpriteSheet(f"{file}\\{image_name}")

				image_names = ["unchecked", "checked"]

				images["checkbox"] = dict(zip(image_names, image.load_strip((0, 0, 10, 10), 2, -1)))

			elif image_name == "arrows.png":

				image = SpriteSheet(f"{file}\\{image_name}")

				image_names = ["left", "right"]

				images["arrows"] = dict(zip(image_names, image.load_strip((0, 0, 8, 7), 2, -1)))

			else:

				images[re.match(r"[^.]+", image_name).group()] = pygame.image.load(f"{file}\\{image_name}").convert_alpha()

		return images

	def close_menus(self):

		for menu in self.menus.values():

			menu.close()

	def change_music(self):

		if os.environ["music"]:

			os.environ["music"] = ""

		else:

			os.environ["music"] = "1"

	def change_hitboxes(self):

		if os.environ["hitboxes"]:

			os.environ["hitboxes"] = ""

		else:

			os.environ["hitboxes"] = "1"


	def change_ambience(self):

		if os.environ["ambience"]:

			os.environ["ambience"] = ""

		else:

			os.environ["ambience"] = "1"

	def change_sfx(self):

		if os.environ["sfx"]:

			os.environ["sfx"] = ""

		else:

			os.environ["sfx"] = "1"

	def change_windowscale(self, direction):

		if os.environ["window_scale"] == "1" and direction == "right":
			self.channels[0].play(self.audio["selectA"])
			os.environ["window_scale"] = "2"

		elif os.environ["window_scale"] == "2" and direction == "left":
			self.channels[0].play(self.audio["selectA"])
			os.environ["window_scale"] = "1"

		pygame.event.post(pygame.event.Event(pygame.VIDEORESIZE, size = (int(os.environ["screen_width"]) * int(os.environ["window_scale"]), int(os.environ["screen_height"]) * int(os.environ["window_scale"])), w = int(os.environ["screen_width"]) * int(os.environ["window_scale"]), h = int(os.environ["screen_height"]) * int(os.environ["window_scale"])))
		
	def change_volume(self, direction):

		volume = round(float(os.environ["volume"]), 1)

		if direction == "right":
			if volume < 1:
				self.channels[0].play(self.audio["selectA"])
				os.environ["volume"] = str(round(volume + 0.1, 1))
			else:
				self.channels[0].play(self.audio["menu_fail"])

		if direction == "left":
			if volume > 0:
				self.channels[0].play(self.audio["selectA"])
				os.environ["volume"] = str(round(volume - 0.1, 1)) 
			else:
				self.channels[0].play(self.audio["menu_fail"])

	def start_new_game(self):

		self.channels[0].play(self.audio["selectA"])
		
		self.current_menu = self.menus["New_Game"]

		self.menus["New_Game"].open()	

	def pause_save_exit(self):

		self.channels[0].play(self.audio["selectA"])
		
		self.current_menu = self.menus["Save_Exit"]

		self.menus["Save_Exit"].open()			

	def pause_options_graphics(self):

		self.channels[0].play(self.audio["selectA"])
		
		self.current_menu = self.menus["Pause_Options_Graphics"]

		self.menus["Pause_Options_Graphics"].open()

	def pause_options_audio(self):

		self.channels[0].play(self.audio["selectA"])
		
		self.current_menu = self.menus["Pause_Options_Audio"]

		self.menus["Pause_Options_Audio"].open()

	def start_options_graphics(self):

		self.channels[0].play(self.audio["selectA"])
		
		self.current_menu = self.menus["Start_Options_Graphics"]

		self.menus["Start_Options_Graphics"].open()

	def start_options_audio(self):

		self.channels[0].play(self.audio["selectA"])

		self.current_menu = self.menus["Start_Options_Audio"]

		self.menus["Start_Options_Audio"].open()

	def pause_options(self):

		self.channels[0].play(self.audio["selectA"])
		
		self.current_menu = self.menus["Pause_Options"]

		self.menus["Pause_Options"].open()

	def start_options(self):

		self.channels[0].play(self.audio["selectA"])
		
		self.current_menu = self.menus["Start_Options"]

		self.menus["Start_Options"].open()		

	def exit(self):

		self.channels[0].play(self.audio["selectA"])

		pygame.event.post(pygame.event.Event(pygame.QUIT))

	def blitme(self):

		for menu in self.menus.values():

			menu.blitme(self.screen)

	def save(self):

		with open("Saves\\save.dat", "wb") as file:

			pickle.dump(self.game_state(), file)

	def save_exit(self):

		self.channels[0].play(self.audio["selectA"])

		with open("Saves\\save.dat", "wb") as file:

			pickle.dump(self.game_state(), file)

		os.environ["start"] = ""

		os.environ["active"] = ""

		os.environ["gaming"] = ""

		os.environ["pause"] = "1"

		self.king.timer.end()

		self.current_menu = None

		self.close_menus

		self.menus = self._load_menus()

		pygame.mixer.stop()

	def new_game(self):

		self.channels[0].play(self.audio["selectA"])

		self.channels[1].play(self.audio["opening_theme"])

		self.king.reset()

		self.levels.reset()

		with open("Saves\\save.dat", "wb") as file:

			pickle.dump(self.game_state(), file)

		os.environ["active"] = "1"

		os.environ["attempt"] = str(int(os.environ.get("attempt")) + 1)

		os.environ["session"] = "0"

		self.close_menus()

		self.current_menu = None	

	def back(self):

		self.channels[0].play(self.audio["selectA"])

		if self.current_menu:

			self.current_menu.close()

			self.current_menu = self.current_menu.parent

		if not self.current_menu:

			os.environ["pause"] = ""

			self.menus["Stat_Menu2"].active = False

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
			self.king.time = state["KING"]["time"]
			self.king.jumps = state["KING"]["jumps"]
			self.king.falls = state["KING"]["falls"]
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

			for flyer in self.levels.flyers.flyers:

				self.levels.flyers.flyers[flyer].x = state["LEVELS"]["flyer_x"][flyer]
				self.levels.flyers.flyers[flyer].y = state["LEVELS"]["flyer_y"][flyer]

			for scrollers in self.levels.scrollers.scrollers:

				for scroller in range(len(self.levels.scrollers.scrollers[scrollers])):

					self.levels.scrollers.scrollers[scrollers][scroller].x = state["LEVELS"]["scroller_x"][scrollers][scroller]
					self.levels.scrollers.scrollers[scrollers][scroller].y = state["LEVELS"]["scroller_y"][scrollers][scroller]

		self.king._update_sprites()

		os.environ["active"] = "1"

		os.environ["session"] = str(int(os.environ.get("session")) + 1)

		self.close_menus()

		self.current_menu = None

	def game_state(self):

		state = {	"KING"	 : {	"x" : self.king.rect_x,
									"y" : self.king.rect_y,
									"speed" : self.king.speed,
									"angle" : self.king.angle,
									"time" : self.king.time,
									"jumps" : self.king.jumps,
									"falls" : self.king.falls,
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
									"flyer_x" : {flyer : self.levels.flyers.flyers[flyer].x for flyer in self.levels.flyers.flyers},
									"flyer_y" : {flyer : self.levels.flyers.flyers[flyer].y for flyer in self.levels.flyers.flyers},
									"scroller_x" : {scrollers : [scroller.x for scroller in self.levels.scrollers.scrollers[scrollers]] for scrollers in self.levels.scrollers.scrollers},
									"scroller_y" : {scrollers : [scroller.y for scroller in self.levels.scrollers.scrollers[scrollers]] for scrollers in self.levels.scrollers.scrollers}
																}
																	}

		return state

	def press_start(self):

		os.environ["start"] = "1"

		self.current_menu.reset()

		self.current_menu.active = False
		
		self.current_menu = self.menus["Start_Menu"]

		self.current_menu.active = True

		self.menus["Stat_Menu1"].active = True

class Menu:

	def __init__(self, parent, title, x, y, images, audio, *buttons):

		self.parent = parent

		self.buttons = list(buttons)

		self.title = title

		self.x, self.y = x, y

		self.images = images

		self.audio = audio

		self.channels = [pygame.mixer.Channel(13), pygame.mixer.Channel(14)]

		self.current_index = 0

		self.blit_counter = 0

		self.active = False

	@property
	def width(self):	
		try:
			if self.title:
				return max([button.width + 60 for button in self.buttons] + [self.title.get_width() + 30]) // 16 * 16
			else:
				return max([button.width + 60 for button in self.buttons]) // 16 * 16
		except:
			return 0

	@property
	def height(self):	
		try:
			if self.title:
				return (len(self.buttons) + 1) * 32

			else:
				return len(self.buttons) * 32
		except:
			return 0
	
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

				if self.blit_counter > 100:

					title_bump = 0

					if self.title:

						frame.blit(self.title, (15, 20))

						title_bump = 1

					for index, button in enumerate(self.buttons):

						if button == self.current_button:

							button.blitme(frame, 15 + self.images["cursor"].get_width(), (index + title_bump + 1) * 20)
							frame.blit(self.images["cursor"], (2, (index + title_bump + 1) * 20 + int(button.height / 2 - self.images["cursor"].get_height() / 2)))

						else:

							button.blitme(frame, 15, (index + title_bump + 1) * 20)

				self.blit_counter += 1

			screen.blit(frame, (self.x, self.y))

		else:

			self.blit_counter = 0

	def update(self):

		pass

	def activate(self, direction):

		self.current_button.activate(direction)

class Stat_Menu(Menu):

	@property
	def current_button(self):

		return None

	def update(self):

		attempt, session = os.environ.get("attempt"), os.environ.get("session")

		time = int(os.environ.get("time"))

		seconds = int(time / 1000 % 60)

		minutes = int(time / (1000 * 60) % 60)

		hours = int(time / (1000 * 60 * 60) % 24)

		self.buttons[0].text = self.buttons[0].font.render(f"ATTEMPT : {attempt} SESSION : {session}", True, (150, 150, 150))

		self.buttons[1].text = self.buttons[1].font.render(f"TIME : {hours}H {minutes}M {seconds}s", True, (150, 150, 150))

		self.buttons[2].text = self.buttons[2].font.render("JUMPS : %s" % os.environ.get("JUMPS"), True, (150, 150, 150))

		self.buttons[3].text = self.buttons[3].font.render("FALLS : %s" % os.environ.get("FALLS"), True, (150, 150, 150))	

class Blinker_Menu:

	def __init__(self, parent, x, y, width, height, images, audio, button):

		self.parent = parent

		self.x, self.y = x, y

		self.images = images

		self.audio = audio

		self.width, self.height = width, height

		self.button = button

		self.channels = [pygame.mixer.Channel(13), pygame.mixer.Channel(14)]

		self.blinking = False

		self.active = False

		self.blink_counter = 0

		self.blit_counter = 0

		self.blit_long_interval = 30

		self.blit_interval = 5

		self.blink_length = 15

	@property
	def current_button(self):

		return None

	def close(self):

		self.active = False

		self.current_index = 0

	def open(self):

		self.active = True

		self.channels[0].play(self.audio["menu_open"])
	
	def update(self):

		if self.blinking and self.blink_counter >= self.blink_length:

			self.button.activate("space")

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

	def activate(self, direction):

		if direction == "space":

			if not self.blinking:

					self.channels[0].play(self.audio["press_start"])

			self.blinking = True

class Button:

	def __init__(self, font, text, function):

		self.font = font

		self.text = text

		self.function = function

	@property
	def width(self):
		if self.text:
			return self.text.get_width()
		else:
			return 0

	@property	
	def height(self):
		if self.text:
			return self.text.get_height()
		else:
			return 0

	def blitme(self, screen, x, y):

		screen.blit(self.text, (x, y))

	def activate(self, direction):

		if direction == "space":

			self.function()

class CheckBox(Button):

	def __init__(self, font, text, images, variable, function):

		super().__init__(font, text, function)

		self.variable = variable

		self.images = images

		self.xpadding, self.ypadding = 5, 2

		self._update_status()

	def _update_status(self):

		if os.environ[self.variable]:

			self.status = "checked"

		else:

			self.status = "unchecked"

	@property
	def width(self):

		if self.text:
			return self.text.get_width() + self.images[self.status].get_width()
		else:
			return 0

	def blitme(self, screen, x, y):

		screen.blit(self.text, (x, y))
		screen.blit(self.images[self.status], (x + self.xpadding + self.text.get_width(), y + self.ypadding))

	def activate(self, direction):

		if direction == "space":

			self.function()

			self._update_status()

class Slider:

	def __init__(self, images, variable, function):

		self.function = function

		self.images = images

		self.width, self.height = 9 * 8, 8

		self.variable = variable

	def blitme(self, screen, x, y):

		slider = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

		for i in range(0, self.width, 8):

			if i == 0:

				slider.blit(self.images["left"], (i, 0))

			elif i == self.width - 8:

				slider.blit(self.images["right"], (i, 0))

			else:
	
				slider.blit(self.images["line"], (i, 0))

		slider.blit(self.images["slider"], (4 + int(56 * float(os.environ[self.variable])), 0))

		screen.blit(slider, (x, y))

	def activate(self, direction):

		self.function(direction)

class Number_Slider:

	def __init__(self, font, images, variable, function):

		self.font = font

		self.function = function

		self.images = images

		self.variable = variable

	@property
	def text(self):
		return self.font.render(os.environ[self.variable] + "x", True, (255, 255, 255))

	@property
	def width(self):
		return self.text.get_width() + self.images["left"].get_width() * 2

	@property
	def height(self):
		return self.text.get_height()

	def blitme(self, screen, x, y):

		screen.blit(self.images["left"], (x, y + self.images["left"].get_height() / 2))
		screen.blit(self.text, (x + 2 + self.images["left"].get_width(), y))
		screen.blit(self.images["right"], (x + self.text.get_width() + self.images["left"].get_width() + 2, y + self.images["left"].get_height() / 2))

	def activate(self, direction):

		self.function(direction)
	
	








