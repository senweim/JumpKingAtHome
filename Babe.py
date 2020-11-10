#!/usr/bin/env python
#
#
#
#

import pygame
import math
import os
from King import King
from Timer import Timer
from physics import Physics
from spritesheet import SpriteSheet
from BabeSprites import Babe_Sprites
from Babe_Audio import Babe_Audio
from King_Particles import King_Particle

class Babe(King):

	def __init__(self, screen, levels):

		self.screen = screen

		self.sprites = Babe_Sprites().babe_images

		self.levels = levels

		self.level = self.levels.max_level

		self.timer = Timer()

		# Booleans

		self.isWalk = False

		self.isCrouch = False

		self.isFalling = False

		self.isKiss = False

		self.hasKissed = False

		self.collideBottom = False

		self.lastCollision = True

		# Animation

		self.walkCount = 0

		self.x, self.y = 375, 113

		self.width, self.height = 32, 32

		self.rect_x, self.rect_y = self.x + 1, self.y + 7

		self.rect_width, self.rect_height = self.width - 12, self.height - 8

		self.current_image = self.sprites["Babe_Stand1"]

		# Particles

		self.jump_particle = King_Particle("images\\particles\\jump_particle.png", 5, 1, 32)

		self.snow_jump_particle = King_Particle("images\\particles\\snow_jump_particle.png", 4, 3, 36)

		self.isJump = False

		self.isLanded = False

		# Audio

		self.channel = pygame.mixer.Channel(10)

		self.audio = Babe_Audio().audio

		# Physics

		self.physics = Physics()

		self.speed, self.angle = 0, 0

		self.maxSpeed = 11

		self.walkAngles = {"right" : math.pi/2, "left" : -math.pi/2}

		self.slip = 0

		# Ending

		self.ending_distance = 50

	def blitme(self):

		self.x = self.rect.x - 6
		self.y = self.rect.y - 9

		if self.levels.current_level == self.level:
			self.screen.blit(self.current_image, (self.x, self.y))

			# pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 1)

	def update(self, king, command = None):

		if self.levels.current_level == self.level:

			self._check_events(command)

			self._update_audio1()

			self._add_gravity()

			self._move()

			self._check_collisions()

			self._update_vectors()

			self._update_sprites()

			self._update_audio2()

			self._update_particles()

			if not self.levels.ending:

				self._check_ending(king)

	def _check_ending(self, king):

		if self.rect_y - king.rect_y >= 0:

			if self.rect_x - king.rect_x <= self.ending_distance:

				self.levels.ending = True

				king.rect_x, king.rect_y = self.rect_x - self.ending_distance, self.rect_y 

				king.speed = 0

	def _check_events(self, command):

		if command:

			if command == "Crouch" and not self.isCrouch:

				self.timer.start()

				self.isCrouch = True

			elif command == "Jump":

				self._jump()

			elif command == "Kiss":

				self.isKiss = True

			elif command == "WalkLeft":

				self._walk("left")

			elif command == "WalkRight":

				self._walk("right")

			elif command == "Snatched":

				self.rect_y += 999

		else:

			self.isKiss = False
			self.hasKissed = False

	def _move(self):

		if self.speed > self.maxSpeed:
			self.speed = self.maxSpeed

		self.rect_x += math.sin(self.angle) * self.speed
		self.rect_y -= math.cos(self.angle) * self.speed

	# def _check_collisions(self):

	# 	self.isFalling = True

	# 	self.collideBottom = False
	# 	self.slip = 0

	# 	for platform in self.levels.levels[self.levels.current_level].platforms:
			
	# 		if self._collide_rect(self.rect, platform):

	# 			if self.rect.bottom >= platform.top and round(self.rect.bottom - platform.top) <= round(self.speed) and -math.cos(self.angle) > 0 and not platform.support:

	# 				self.rect.bottom = platform.top
	# 				self.isFalling = False
	# 				self.isContact = False
	# 				self.collideBottom = True

	# 				if not self.lastCollision:
	# 					self.isLanded = True

	# 				self.lastCollision = platform
	# 				self.slip = platform.slip

	# 	if not self.collideBottom:

	# 		self.lastCollision = None

	def _update_vectors(self):

		if self.collideBottom:

			self.angle, self.speed = self.physics.add_vectors(self.angle, self.speed, -self.physics.gravity[0], -self.physics.gravity[1])

			self.speed *= self.slip

	def _walk(self, direction):

		self.speed = 1
		self.angle = self.walkAngles[direction]
		self.isWalk = True

	def _jump(self):

		speed = (2 + (self.timer.elapsed_time()*2) / 150)
		angle = 0

		self.angle, self.speed = self.physics.add_vectors(self.angle, self.speed, angle, speed)

		self.isJump = True
		self.isCrouch = False
		self.isWalk = False
		self.timer.end()

	def _update_sprites(self):

		if self.isCrouch:

			self.current_image = self.sprites["Babe_Crouch"]

		if self.isFalling:

			if self.angle < math.pi/2 or self.angle > 3 * math.pi / 2:

				self.current_image = self.sprites["Babe_Jump"]

			else:

				self.current_image = self.sprites["Babe_Fall"]

		elif self.isKiss:

			self.current_image = self.sprites["Babe_Kiss"]

		elif self.lastCollision and self.isLanded:

			self.current_image = self.sprites["Babe_Land"]

		else:

			if self.walkCount <= 5:

				self.current_image = self.sprites["Babe_Stand1"]

			elif self.walkCount <= 8:

				self.current_image = self.sprites["Babe_Stand2"]

			elif self.walkCount <= 13:

				self.current_image = self.sprites["Babe_Stand3"]

			else:

				self.walkCount = 0

			self.walkCount += 1	

	def _update_audio1(self):

		if self.lastCollision:

			if self.isJump:

				self.channel.play(self.audio["babe_jump"])

	def _update_audio2(self):

		if self.lastCollision:

			if self.isLanded:

				self.channel.play(self.audio["king_land"])

				self.isLanded = False

		if self.isKiss:

			if not self.channel.get_busy() and not self.hasKissed:

				self.channel.play(self.audio["babe_kiss"])

				self.hasKissed = True
