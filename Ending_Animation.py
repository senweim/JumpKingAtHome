#!/usr/bin/env python
#
#
#
#

import pygame
import os
import sys
import math

class Ending_Animation:

	def __init__(self):

		self.scale = int(os.environ.get("resolution"))

		self.end_counter = 0

		self.end_pan = (-90 * self.scale, 90 * self.scale)

		self.stall_x = 240 * self.scale

		self.stall_y = 220 * self.scale

		self.channel = pygame.mixer.Channel(14)

		self.ending_music = pygame.mixer.Sound("Audio\\Misc\\ending.wav")

		self.end_image = pygame.image.load("imagecrown.png")

		self.end_image = pygame.transform.scale(self.end_image, (self.end_image.get_width() * self.scale, self.end_image.get_height() * self.scale))

	def update(self, level, king, babe):

		king_command = None
		babe_command = None

		if self.move_screen(level, king, babe):		

			if self.end_counter < 50:

				pass

			elif self.end_counter == 50:

				babe_command = "Crouch"

			elif self.end_counter < 60:

				pass

			elif self.end_counter == 60:

				babe_command = "Jump"

			elif self.end_counter <= 120:

				pass

			elif self.end_counter <= 150:

				babe_command = "WalkLeft"

			elif self.end_counter <= 175:

				babe_command = "Kiss"

			elif self.end_counter <= 190:

				level.flyer.active = True

			elif self.end_counter <= 205:
				
				king_command = "LookUp"
				babe_command = "WalkRight"

			elif self.end_counter == 330:

				king_command = "Crouch"

			elif self.end_counter == 350:

				king_command = "Jump"

			elif self.end_counter <= 420:

				if king.y <= level.flyer.rect.bottom:

					king.isWearingCrown = True
					king.rect.top = level.flyer.rect.bottom + (king.rect.top - king.y - 3 * self.scale)
					king_command = "Freeze"

				if self.end_counter == 360:
					level.flyer.channel.play(level.flyer.audio)

			elif self.end_counter <= 460:

				level.flyer.active = False

			elif self.end_counter <= 500:

				king.isHoldingUpHands = True

			elif self.end_counter == 501:

				king.isSnatch = True

			elif self.end_counter == 502:

				king.isSnatch = False
				king.isHoldingBabe = True
				babe_command = "Snatched"
				babe.channel.play(babe.audio["babe_pickup"])

			elif self.end_counter <= 670:

				king_command = "WalkLeft"

			elif self.end_counter <= 730:

				pass

			elif self.end_counter <= 820:

				if self.end_counter == 731:
					babe.channel.play(babe.audio["babe_surprised2"])

				self.scroll_screen(level, king)
				king_command = "WalkRight"
				king.update(king_command)

			elif self.end_counter == 821:

				self.scroll_screen(level, king)
				king_command = "Crouch"

			elif self.end_counter == 862:

				babe.channel.play(babe.audio["babe_jump"])

				self.scroll_screen(level, king)
				king_command = "JumpRight"

			elif self.end_counter <= 1700:

				self.scroll_screen(level, king)

				if self.end_counter == 930:

					king.channel.play(king.audio["Land"]["king_jump"])

				if self.end_counter > 1000:

					king.isAdmiring = True

					if self.end_counter == 1100:

						babe.channel.play(babe.audio["babe_mou"])

				if self.end_counter > 1200:

					king.isAdmiring = False

			else:

				if self.end_counter > 3000:

					sys.exit()

				return True
				
			self.end_counter += 1

		king.update(king_command)

		babe.update(king, babe_command)

	def scroll_screen(self, level, king):

		if king.rect.x > self.stall_x:

			rel_x = king.rect.x - self.stall_x

			king.rect.x -= rel_x

			if level.midground:
				level.midground.rect.move_ip(-rel_x, 0)

			if level.props:
				for prop in level.props:
					prop.rect.move_ip(-rel_x, 0)

			if level.npc:
				level.npc.rect.move_ip(-rel_x, 0)	

			if level.foreground:
				level.foreground.rect.move_ip(-rel_x, 0)

			if level.platforms:
				for platform in level.platforms:
					platform.move_ip(-rel_x, 0)		

		if king.rect.y > self.stall_y:

			rel_y = king.rect.y - self.stall_y

			if self.stall_y > level.screen.get_height() / 2:

				self.stall_y -= 2 * self.scale

			king.rect.y -= rel_y

			if level.midground:
				level.midground.rect.move_ip(0, -math.sqrt(rel_y))

			if level.props:
				for prop in level.props:
					prop.rect.move_ip(0, -math.sqrt(rel_y))

			if level.npc:
				level.npc.rect.move_ip(0, -math.sqrt(rel_y))	

			if level.foreground:
				level.foreground.rect.move_ip(0, -math.sqrt(rel_y))

			if level.platforms:
				for platform in level.platforms:
					platform.move_ip(0, -math.sqrt(rel_y))		

	def move_screen(self, level, king, babe):

		if self.end_pan[0] != 0 or self.end_pan[1] != 0:

			try:
				x = self.end_pan[0]/abs(self.end_pan[0]) / 2 * self.scale
			except ZeroDivisionError:
				x = 0
			try:
				y = self.end_pan[1]/abs(self.end_pan[1]) / 2 * self.scale
			except ZeroDivisionError:
				y = 0

			if level.midground:

				level.midground.rect.move_ip(x, y)

			if level.props:
				for prop in level.props:
					prop.rect.move_ip(x, y)

			if level.npc:
				level.npc.rect.move_ip(x, y)	

			if level.foreground:
				level.foreground.rect.move_ip(x, y)

			if level.platforms:
				for platform in level.platforms:
					platform.move_ip(x, y)

			king.rect.move_ip(x, y)

			babe.rect.move_ip(x, y)

			self.end_pan = (self.end_pan[0] - x, self.end_pan[1] - y)

			return False

		else:

			return True

	def update_audio(self):

		try:

			if not self.channel.get_busy():

				self.channel.play(self.ending_music)

		except Exception as e:

			print("ENDINGUPDATEAUDIO ERROR: ", e)


	def blitme(self, screen):

		screen.blit(self.end_image, (0, 0))