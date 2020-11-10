#!/usr/bin/env python
#
#
#
#

import pygame
import collections
import os
import math
import sys
from hiddenwalls import HiddenWalls
from Platforms import Platforms
from Background import Backgrounds
from Props import Props
from weather import Weathers
from scrolling import Scrollers
from BackgroundMusic import BackgroundAudio
from NPC import NPCs
from Names import Names
from Readable import Readables
from Flyers import Flyers
from Ending_Animation import Ending_Animation
from Wind import Wind

class Level:

	def __init__(self, screen, level):

		self.screen = screen

		self.level = level

		self.found = False

		self.platforms = None

		self.background = None

		self.midground = None

		self.foreground = None

		self.weather = None

		self.hiddenwalls = None

		self.props = None

		self.scrollers = None

		self.shake = None

		self.background_audio = None

		self.npc = None     

		self.name = None

		self.readable = None

		self.flyer = None

class Levels:

	def __init__(self, screen):

		self.max_level = 42

		self.current_level = 0

		self.current_level_name = None

		self.screen = screen

		# Objects

		self.platforms = Platforms()

		self.background = Backgrounds("BG").backgrounds

		self.midground = Backgrounds("MG").backgrounds

		self.foreground = Backgrounds("FG").backgrounds

		self.props = Props().props

		self.weather = Weathers().weather

		self.hiddenwalls = HiddenWalls().hiddenwalls

		self.scrollers = Scrollers()

		self.npcs = NPCs().npcs

		self.names = Names()

		self.readables = Readables().readables

		self.flyers = Flyers()

		self.Ending_Animation = Ending_Animation()

		# Audio

		self.background_audio = BackgroundAudio().level_audio

		self.channels = [pygame.mixer.Channel(2), pygame.mixer.Channel(3), pygame.mixer.Channel(4), pygame.mixer.Channel(5)]

		for channel in self.channels:

			channel.set_volume(1.0)

		# Movement 

		self.shake_var = 0

		self.shake_levels = [39, 40, 41]

		self.wind = Wind(self.screen)

		self.levels = {}

		self._load_levels()

		# Ending

		self.ending = False

		self.END = False

	def blit1(self):

		try:

			current_level = self.levels[self.current_level]

			if current_level.background:
				current_level.background.blitme(self.screen)

			if current_level.scrollers:
				for scroller in current_level.scrollers:
					scroller.blitme(self.screen, "bg")

			if current_level.midground:
				current_level.midground.blitme(self.screen)

			if current_level.props:
				for prop in current_level.props:
						prop.blitme(self.screen)

			if current_level.flyer:
				current_level.flyer.blitme(self.screen)

			if current_level.npc:
				current_level.npc.blitme(self.screen)

			if current_level.weather:
				current_level.weather.blitme(self.screen, self.wind.rect)

		except Exception as e:
			
			print("BLIT1 ERROR: ", e)

	def blit2(self):

		try:

			current_level = self.levels[self.current_level]

			if current_level.foreground:
				current_level.foreground.blitme(self.screen)
			
			if current_level.hiddenwalls:
				for hiddenwall in current_level.hiddenwalls:
					hiddenwall.blitme(self.screen)

			if current_level.scrollers:
				for scroller in current_level.scrollers:
					scroller.blitme(self.screen, "fg")

			if current_level.npc:
				current_level.npc.blitmetext(self.screen)

			if current_level.readable:
				current_level.readable.blitmetext(self.screen)

			if self.names.active:
				self.names.blitme(self.screen)

			if os.environ.get("hitboxes"):
				if current_level.platforms:
					for platform in current_level.platforms:
						pygame.draw.rect(self.screen, (255, 0, 0), platform.rect, 1)

			if self.END:

				self.Ending_Animation.blitme(self.screen)

			
		except Exception as e:

			print("BLIT2 ERROR: ", e)

	def update_levels(self, king, babe, agentCommand=None):

		self.update_wind(king)

		self.update_hiddenwalls(king)

		self.update_npcs(king)

		self.update_readables(king)

		self.update_flyers(king)

		self.update_discovery(king)

		self.update_audio()

		if self.ending:

			self.END = self.Ending_Animation.update(self.levels[self.current_level], king, babe)

		else:

			king.update(agentCommand=agentCommand)

			babe.update(king)

	def update_flyers(self, king):

		try:

			current_level = self.levels[self.current_level]

			if current_level.flyer:

				current_level.flyer.update(king)

		except Exception as e:

			print("UPDATEFLYERS ERROR: ", e)

	def update_audio(self):

		try:

			if not self.ending:

				current_level = self.levels[self.current_level]

				for index, audio in enumerate(current_level.background_audio):

					if not audio:

						self.channels[index].stop()

					elif audio != [channel.get_sound() for channel in self.channels][index]:

						self.channels[index].play(audio)

				self.names.play_audio()

			else:

				for channel in self.channels:

					channel.stop()

				self.Ending_Animation.update_audio()

		except Exception as e:

			print("UPDATEAUDIO ERROR: ", e)

	def update_discovery(self, king):

		try:

			if not king.isFalling:

				if self.levels[self.current_level].name != self.current_level_name:

					self.current_level_name = self.levels[self.current_level].name

					if self.current_level_name:

						self.names.opacity = 255

						self.names.active = True

						self.names.blit_name = self.current_level_name

						self.names.blit_type = self.levels[self.current_level].found

				self.levels[self.current_level].found = True

		except Exception as e:

			print("UPDATEDISCOVERY ERROR: ", e)

	def update_readables(self, king):

		try:

			if self.levels[self.current_level].readable:

				self.levels[self.current_level].readable.update(king)

		except Exception as e:

			print("UPDATEREADABLES ERROR:", e)

	def update_npcs(self, king):

		try:

			for npc in self.npcs.values():

				npc.update(king)

		except Exception as e:

			print("UPDATENPCS ERROR:", e)

	def update_hiddenwalls(self, king):

		try:

			if self.levels[self.current_level].hiddenwalls:
				
				for hiddenwall in self.levels[self.current_level].hiddenwalls:
					
					hiddenwall.check_collision(king)

		except Exception as e:

			print("UPDATEHIDDENWALLS ERROR: ", e)

	def update_wind(self, king):

		try:

			wind = self.wind.calculate_wind(king)

			if self.levels[self.current_level].weather:

				if self.levels[self.current_level].weather.hasWind:

					if not king.lastCollision:

						king.angle, king.speed = king.physics.add_vectors(king.angle, king.speed, math.pi / 2, wind / 50)

					elif not king.lastCollision.type == "Snow":

						king.angle, king.speed = king.physics.add_vectors(king.angle, king.speed, math.pi / 2, wind / 50)

		except Exception as e:

			print("UPDATEWIND ERROR: ", e)


	def _load_levels(self):

		try:

			for i in range(0, self.max_level + 1):

				self.levels[i] = Level(self.screen, i)

				try:
					self.levels[i].background = self.background[i]
				except:
					pass

				try:
					self.levels[i].midground = self.midground[i]
				except:
					pass


				try:
					self.levels[i].foreground = self.foreground[i]
				except:
					pass


				try:
					self.levels[i].platforms = self.platforms.platforms(i)
				except:
					pass

				try:
					self.levels[i].props = self.props[i]
				except:
					pass

				try:
					self.levels[i].weather = self.weather[i]
				except:
					pass
				try:
					self.levels[i].hiddenwalls = self.hiddenwalls[i]
				except:
					pass
				try:
					self.levels[i].scrollers = self.scrollers.scrollers[i]
				except:
					pass

				try:
					if i in self.shake_levels:
						self.levels[i].shake = True
				except:
					pass

				try:
					self.levels[i].background_audio = self.background_audio[i]
				except:
					pass

				try:
					self.levels[i].npc = self.npcs[i]
				except:
					pass

				try:
					self.levels[i].name = self.names.names[i]
				except:
					pass

				try:
					self.levels[i].readable = self.readables[i]
				except:
					pass

				try:
					self.levels[i].flyer = self.flyers.flyers[i]
				except:
					pass

		except Exception as e:

			print("LOAD LEVELS ERROR: ", e)

	def reset(self):

		self.current_level = 0

		self.wind.__init__(self.screen)

		self.scrollers.__init__()

		self.flyers.__init__()
