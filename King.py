#!/usr/bin/env python
#
#
#
#

import pygame
import math
import collections
import os
import numpy
import random
from Timer import Timer
from physics import Physics
from spritesheet import SpriteSheet
from King_Sprites import King_Sprites
from King_Particles import King_Particle
from King_Audio import King_Audio

# action list
def get_action_dict(agentCommand):
	keys = {}
	if agentCommand == 0:
		keys[pygame.K_SPACE] = 0
		keys[pygame.K_RIGHT] = 1
		keys[pygame.K_LEFT] = 0

	elif agentCommand == 1:
		keys[pygame.K_SPACE] = 0
		keys[pygame.K_RIGHT] = 0
		keys[pygame.K_LEFT] = 1

	elif agentCommand == 2:
		keys[pygame.K_SPACE] = 1
		keys[pygame.K_RIGHT] = 1
		keys[pygame.K_LEFT] = 0

	elif agentCommand == 3:
		keys[pygame.K_SPACE] = 1
		keys[pygame.K_RIGHT] = 0
		keys[pygame.K_LEFT] = 1

	# elif agentCommand == 4:
	# 	keys[pygame.K_SPACE] = 0
	# 	keys[pygame.K_RIGHT] = 0
	# 	keys[pygame.K_LEFT] = 0
	#
	# elif agentCommand == 5:
	# 	keys[pygame.K_SPACE] = 1
	# 	keys[pygame.K_RIGHT] = 0
	# 	keys[pygame.K_LEFT] = 0

	else:
		print(agentCommand)
		raise ValueError('Invalid action')

	return keys



class King():

	""" represents the king """

	def __init__(self, screen, levels):

		# Static 

		self.screen = screen

		self.sprites = King_Sprites().king_images

		self.levels = levels

		self.timer = Timer()

		self.creative_speed = 10

		self.walkAngles = {"right" : math.pi/2, "left" : -math.pi/2}

		self.jumpAngles = {'up' : 0, 'left' : -math.pi/3, 'right' : math.pi/3}

		# Booleans

		self.isWalk = False

		self.isCrouch = False

		self.isFalling = False

		self.isContact = False

		self.isSplat = True

		self.isDance = False

		self.isLookUp = False

		self.isSnatch = False

		self.isHoldingUpHands = False

		self.isHoldingBabe = False

		self.isAdmiring = False

		self.isWearingCrown = False

		self.collided = False

		self.jumpParticle = False

		self.lastCollision = None

		self.collideTop = False

		self.collideRight = False

		self.collideLeft = False

		self.collideBottom = False

		self.collideRamp = False

		self.isJump = False

		self.isLanded = False

		# Stats

		self.time = 0

		self.jumps = 0

		self.falls = 0

		# Animation

		self.x, self.y = 230, 298

		self.width, self.height = 32, 32

		self.rect_x, self.rect_y = self.x + 1, self.y + 7

		self.rect_width, self.rect_height = self.width - 12, self.height - 8

		self.direction = "right"

		self.danceCount = 0

		self.walkCount = 0

		self.jumpCount = 0

		self.splatCount = 0

		self.umbrellaCount = 0

		self.maxJumpCount = 30

		self.walkSpeed = 1.4

		self.maxSpeed = 11

		self.maxSlopeSpeed = 7
 
		self.idle_counter = 0

		self.idle_time = 300

		self.idle_length = 200

		self.splatDuration = 0

		self.current_image = self.sprites[self.direction]["King_Fell"]

		self.mask = pygame.mask.from_surface(self.current_image)

		# Particles

		self.jump_particle = King_Particle("images\\particles\\jump_particle.png", 5, 1, 32)

		self.snow_jump_particle = King_Particle("images\\particles\\snow_jump_particle.png", 4, 3, 36)

		self.level_change = 0

		# Audio

		self.channel = pygame.mixer.Channel(7)

		self.audio = King_Audio().audio

		# Physics

		self.physics = Physics()

		self.speed, self.angle = 0, 0

		self.elasticity, self.angle_elasticity = 0.925, 0.5

		self.charge_time = 0

	@property
	def rect(self):

		return pygame.Rect((self.rect_x, self.rect_y, self.rect_width, self.rect_height))

	def blitme(self):

		self.x = self.rect.x - 5
		self.y = self.rect.y - 9

		if self.direction == "left":
			self.x -= 1

		if self.isFalling:

			self.y += 4

			if self.isHoldingBabe:

				self.x -= 30
				self.y -= 30

		self.screen.blit(self.current_image, (self.x, self.y))

		if os.environ.get("hitboxes"):
			pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 1)

		if not self.level_change:

			self.jump_particle.blitme(self.screen)

			self.snow_jump_particle.blitme(self.screen)

		else:

			self.jump_particle.reset()

			self.snow_jump_particle.reset()


	def update(self, command=None, agentCommand=None):

		if os.environ.get("mode") == "normal":

			if not self.isFalling and not self.levels.ending:

				self._check_events(agentCommand)

			elif self.levels.ending:

				self._robot_check_events(command)

			self._update_audio1()

			self._update_particles()

			self._add_gravity()

			self._move()

			self._check_collisions()

			self._update_vectors()

			self._update_sprites()

			self._update_audio2()

			self._check_level()

			self._update_timer()

			self._update_stats()

		else:

			self._creative()

			self._check_level()

			self._update_sprites()

	def _robot_check_events(self, command):

		if command:

			if command == "Crouch":

				self.jumpCount += 1
				self.isCrouch = True

			elif command == "Jump":

				self._jump("up")

			elif command == "Freeze":

				self.angle, self.speed = 0, 0
				self.angle, self.speed = self.physics.add_vectors(self.angle, self.speed, -self.physics.gravity[0], -self.physics.gravity[1])

			elif command == "WalkLeft":

				self._walk("left")

			elif command == "WalkRight":

				self._walk("right")

			elif command == "JumpRight":

				self._jump("right")

		else:

			self.isWalk = False

	def _check_events(self, agentCommand=None):
			if agentCommand is not None:
				keys = get_action_dict(agentCommand)
			else:
				keys = pygame.key.get_pressed()

			if not self.isSplat or self.splatCount > self.splatDuration:

				if keys[pygame.K_SPACE]:
					self.splatCount = 0
					self.idle_counter = 0
					self.jumpCount += 1

					if not self.isCrouch:

						self.isCrouch = True

					elif self.jumpCount > self.maxJumpCount:

						if keys[pygame.K_RIGHT]:

							self._jump("right")

						elif keys[pygame.K_LEFT]:

							self._jump("left")
						else:
							self._jump("up")

				else:

					if keys[pygame.K_RIGHT]:
						self.splatCount = 0
						self.idle_counter = 0

						# Walk
						if not self.isCrouch:
							self._walk("right")
						# Jump
						else:
							self._jump("right")

					elif keys[pygame.K_LEFT]:
						self.splatCount = 0
						self.idle_counter = 0

						#Walk
						if not self.isCrouch:
							self._walk("left")
						#Jump
						else:
							self._jump("left")
					else:

						self.idle_counter += 1

						self.isWalk = False

						if self.isCrouch:
							self._jump("up")

			else:

				self.splatCount += 1

	def _add_gravity(self):

		self.angle, self.speed = self.physics.add_vectors(self.angle, self.speed, self.physics.gravity[0], self.physics.gravity[1])

	def _move(self):

		if self.speed > self.maxSpeed:
			self.speed = self.maxSpeed

		x, y = self.rect_x, self.rect_y

		self.rect_x += math.sin(self.angle) * self.speed
		self.rect_y -= math.cos(self.angle) * self.speed

		#self.rect.move_ip(round(math.sin(self.angle) * self.speed), round(-math.cos(self.angle) * self.speed))

		if self.rect_x != x or abs(self.rect_y - y) > 1:
			self.idle_counter = 0
			self.isLookUp = False
			self.isDance = False
			self.danceCount = 0

	def _collide_right(self, platform):

		rect = self.rect

		if (
			self.rect_x + self.rect_width > platform.rect.left > self.rect_x
			and (platform.rect.top < rect.y < platform.rect.bottom 
				or platform.rect.top < rect.y + rect.height < platform.rect.bottom 
				or rect.y < platform.rect.top < rect.y + rect.height 
				or rect.y < platform.rect.bottom < rect.y + rect.height) 
			and round(rect.x + rect.width - platform.rect.left, 4) <= math.ceil(math.sin(self.angle) * self.speed)
			#and round(math.sin(self.angle), 4) > 0
		):
			return True
		else:

			return False

	def _collide_left(self, platform):

		rect = self.rect

		if (
			self.rect_x < platform.rect.right < self.rect_x + self.rect_width
			and (platform.rect.top < rect.y < platform.rect.bottom 
				or platform.rect.top < rect.y + rect.height < platform.rect.bottom 
				or rect.y < platform.rect.top < rect.y + rect.height 
				or rect.y < platform.rect.bottom < rect.y + rect.height) 
			and round(rect.x - platform.rect.right, 4) >= math.floor(math.sin(self.angle) * self.speed)
			#and round(math.sin(self.angle), 4) < 0
		):
			return True
		else:

			return False

	def _collide_top(self, platform):

		if (
			self.rect_y < platform.rect.bottom < self.rect_y + self.rect_height
			and (platform.rect.left < self.rect_x < platform.rect.right 
				or platform.rect.left < self.rect_x + self.rect_width < platform.rect.right 
				or self.rect_x < platform.rect.left < self.rect_x + self.rect_width 
				or self.rect_x < platform.rect.right < self.rect_x + self.rect_width) 
			and round(self.rect_y - platform.rect.bottom, 4) >= math.floor(-math.cos(self.angle) * self.speed)
			#and round(-math.cos(self.angle), 4) < 0
		):
			return True
		else:
			return False

	def _collide_bottom(self, platform):

		if (
			self.rect_y + self.rect_height > platform.rect.top > self.rect_y
			and (platform.rect.left < self.rect_x < platform.rect.right 
				or platform.rect.left < self.rect_x + self.rect_width < platform.rect.right 
				or self.rect_x < platform.rect.left < self.rect_x + self.rect_width 
				or self.rect_x < platform.rect.right < self.rect_x + self.rect_width)
			and round(self.rect_y + self.rect_height - platform.rect.top, 4) <= math.ceil(-math.cos(self.angle) * self.speed)
			#and round(-math.cos(self.angle), 4) > 0
		):
			return True
		else:
			return False

	def _collide_slope_bottom(self, platform, rel_x):

		if rel_x > platform.rect.width:

			rel_x = platform.rect.width

		rel_y = platform.rect.bottom - (platform.rect.bottom - platform.rect.top)/(platform.rect.right - platform.rect.left)*(rel_x)

		if (
			self.rect_y + self.rect_height > rel_y > self.rect_y
			and (platform.rect.left < self.rect_x < platform.rect.right 
				or platform.rect.left < self.rect_x + self.rect_width < platform.rect.right 
				or self.rect_x < platform.rect.left < self.rect_x + self.rect_width 
				or self.rect_x < platform.rect.right < self.rect_x + self.rect_width)
		):
			return True
		else:
			return False

	def _collide_slope_top(self, platform, rel_x):

		if rel_x > platform.rect.width:

			rel_x = platform.rect.width

		rel_y = platform.rect.top + (platform.rect.bottom - platform.rect.top)/(platform.rect.right - platform.rect.left)*(rel_x)

		if (
			self.rect_y < rel_y < self.rect_y + self.rect_height
			and (platform.rect.left < self.rect_x < platform.rect.right 
				or platform.rect.left < self.rect_x + self.rect_width < platform.rect.right 
				or self.rect_x < platform.rect.left < self.rect_x + self.rect_width 
				or self.rect_x < platform.rect.right < self.rect_x + self.rect_width)
		):
			return True
		else:
			return False
	
	def _check_collisions(self):

		self.isFalling = True

		self.collideTop = False
		self.collideRight = False
		self.collideLeft = False
		self.collideBottom = False
		self.collideRamp = False
		self.slip = 0
		self.slope = 0

		for platform in self.levels.levels[self.levels.current_level].platforms:

			if not platform.slope:

				if self._collide_left(platform):

					self.rect_x = platform.rect.right
					self.lastCollision = platform
					self.collided = True
					self.collideRight = True

				elif self._collide_right(platform):

					self.rect_x = platform.rect.left - self.rect_width
					self.lastCollision = platform
					self.collided = True
					self.collideLeft = True

				elif self._collide_top(platform):
					self.rect_y = platform.rect.bottom
					self.lastCollision = platform
					self.collideTop = True

				elif self._collide_bottom(platform):

					self.slip = platform.slip 
					self.rect_y = platform.rect.top - self.rect_height
					self.isFalling = False
					self.collided = False
					self.isContact = False
					self.collideBottom = True

					if not self.lastCollision:
						self.isLanded = True
						if self.speed >= self.maxSpeed:
							self.isSplat = True
							self.isWalk = False
							self.isJump = False
							self.isDance = False
							self.falls += 1

					self.lastCollision = platform
					self.level_change = 0

			if platform.slope:

				if platform.slope[1] > 0:

					if platform.slope[0] > 0:

						rel_x = self.rect_x + self.rect_width - platform.rect.left

						if self._collide_left(platform):

							self.rect_x = platform.rect.right
							self.lastCollision = platform
							self.collided = True
							self.collideRight = True

						elif self._collide_right(platform) and self.rect_y + self.rect_height > platform.rect.bottom:

							self.rect_x = platform.rect.left - self.rect_width
							self.lastCollision = platform
							self.collided = True
							self.collideLeft = True

						elif self._collide_top(platform):

							self.rect_y = platform.rect.bottom
							self.lastCollision = platform
							self.collideTop = True

						elif self._collide_slope_bottom(platform, rel_x):

							# if self.rect_x + self.rect_width < platform.right:

							while self._collide_slope_bottom(platform, rel_x):

								if self.isFalling:
									self.rect_y -= 1
									self.rect_x -= 1
								else:
									self.rect_x -= 1

								rel_x = self.rect_x + self.rect_width - platform.rect.left

							#else:

							#	self.rect_y = platform.top - self.rect_height			

							self.lastCollision = platform
							self.collideRamp = True
							self.slope = platform.slope[0]
							self.slip = platform.slip

					if platform.slope[0] < 0:

						rel_x = platform.rect.right - self.rect_x

						if self._collide_right(platform):

							self.rect_x = platform.rect.left - self.rect_width
							self.lastCollision = platform
							self.collided = True
							self.collideLeft = True

						elif self._collide_left(platform) and self.rect_y + self.rect_height > platform.rect.bottom:

							self.rect_x = platform.rect.right
							self.lastCollision = platform
							self.collided = True
							self.collideRight = True

						elif self._collide_top(platform):

							self.rect_y = platform.bottom
							self.lastCollision = platform
							self.collideTop = True

						elif self._collide_slope_bottom(platform, rel_x):

							# if self.rect_x > platform.left:

							while self._collide_slope_bottom(platform, rel_x):

								if self.isFalling:
									self.rect_x += 1
									self.rect_y -= 1
								else:
									self.rect_x += 1

								rel_x = platform.rect.right - self.rect_x

							#else:

							#	self.rect_y = platform.top - self.rect_height

							self.lastCollision = platform
							self.collideRamp = True
							self.slope = platform.slope[0]
							self.slip = platform.slip

				if platform.slope[1] < 0:

					if platform.slope[0] < 0:

						rel_x = self.rect_x + self.rect_width - platform.rect.left

						if self._collide_left(platform):

							self.rect_x = platform.rect.right
							self.lastCollision = platform
							self.collided = True
							self.collideRight = True

						elif self._collide_right(platform) and self.rect_y < platform.rect.top:

							self.rect_x = platform.rect.left - self.rect_width
							self.lastCollision = platform
							self.collided = True
							self.collideLeft = True

						elif self._collide_bottom(platform):

							self.rect_y = platform.rect.bottom
							self.lastCollision = platform
							self.collideTop = True

						elif self._collide_slope_top(platform, rel_x):

							while self._collide_slope_top(platform, rel_x):

								self.rect_x -= 1

								rel_x = self.rect_x + self.rect_width - platform.rect.left

							# else:

							# 	self.rect_y = platform.top - self.rect_height			

							self.collided = True
							self.collideTop = True
							self.lastCollision = platform

					if platform.slope[0] > 0:

						rel_x = platform.rect.right - self.rect_x

						if self._collide_right(platform):

							self.rect_x = platform.rect.left - self.rect_width
							self.lastCollision = platform
							self.collided = True
							self.collideLeft = True

						elif self._collide_left(platform) and self.rect_y < platform.rect.top:

							self.rect_x = platform.rect.right
							self.lastCollision = platform
							self.collided = True
							self.collideRight = True

						elif self._collide_bottom(platform):

							self.rect_y = platform.rect.bottom
							self.lastCollision = platform
							self.collideTop = True

						elif self._collide_slope_top(platform, rel_x):

							while self._collide_slope_top(platform, rel_x):

								self.rect_x += 1

								rel_x = platform.rect.right - self.rect_x

							# else:

							# 	self.rect_y = platform.top - self.rect_height

							self.collided = True
							self.collideTop = True
							self.lastCollision = platform
		
		#Hits The Sides

		if self.rect_x + self.rect_width > self.screen.get_width():

			self.rect_x = self.screen.get_width() - self.rect_width
			self.collideRight = True
			self.collided = True

		if self.rect_x < 0:
			self.rect_x = 0
			self.collideLeft = True
			self.collided = True

		if not any([self.collideTop, self.collideRight, self.collideLeft, self.collideBottom, self.collideRamp]):
			self.lastCollision = None

	def _update_vectors(self):

		if self.collideRamp and not self.collideBottom:

			if math.cos(self.angle) * self.slope > 0:

				if self.slope < 0:
					self.angle = 3 * math.pi / 4

				else:
					self.angle = math.pi / 4

			else:

				if self.slope < 0:
					self.angle = 7 * math.pi / 4

				else:

					self.angle = 5 * math.pi / 4

			self.angle, self.speed = self.physics.add_vectors(self.angle, self.speed, 7 * math.pi / 4 * self.slope, self.physics.gravity[1])
			self.angle, self.speed = self.physics.add_vectors(self.angle, self.speed, 5 * math.pi / 4 * self.slope, self.physics.gravity[1])

			if not self.slip:
				self.speed -= 0.35
			else:
				self.speed -= 0.10

			if self.speed > self.maxSlopeSpeed:
				self.speed = self.maxSlopeSpeed

		if self.isFalling:

			if self.collideTop:
				self.angle = math.pi - self.angle
				self.speed *= self.elasticity/2

			if self.collideRight or self.collideLeft:

				if round(-math.cos(self.angle), 4) <= 0:
					self.angle = -self.angle * self.angle_elasticity

				elif round(-math.cos(self.angle), 4) > 0:
					self.angle = math.pi + (math.pi - self.angle) * self.angle_elasticity

				self.speed *= self.elasticity

			self.isCrouch = False

		if self.collideBottom:

			self.angle, self.speed = self.physics.add_vectors(self.angle, self.speed, -self.physics.gravity[0], -self.physics.gravity[1])

			self.speed *= self.slip

	def _check_level(self):

		if self.rect_y < 0 and self.levels.current_level < self.levels.max_level:

			self.rect_y += self.screen.get_height() + self.rect_width
			self.levels.current_level += 1
			self.level_change += 1

		if self.rect_y > self.screen.get_height():

			self.rect_y -= self.screen.get_height() + self.rect_width
			self.levels.current_level -= 1
			self.level_change -= 1

	def _walk(self, direction):

		if self.lastCollision:
			if not self.lastCollision.snow:

				self.speed = self.walkSpeed
				self.angle = self.walkAngles[direction]
				self.isWalk = True

		self.isSplat = False
		self.direction = direction

	def _jump(self, direction):

		speed = (1.5 + ((self.jumpCount/5)**1.13))

		if direction == "up":
			angle = 0

		else:

			angle = self.jumpAngles[direction] * (1 - self.jumpCount / 45.5)
			speed += 0.9

		if direction != "up":
			self.direction = direction

		if self.lastCollision.snow:

			if speed > 2.5:
				self.angle, self.speed = self.physics.add_vectors(self.angle, self.speed, angle, speed)

		else:
			self.angle, self.speed = self.physics.add_vectors(self.angle, self.speed, angle, speed)

		self.isSplat = False
		self.isJump = True
		self.isCrouch = False
		self.isWalk = False
		self.jumpCount = 0
		self.jumps += 1

	def _creative(self):

		keys = pygame.key.get_pressed()

		if keys[pygame.K_UP]:

			self.rect_y -= self.creative_speed

		if keys[pygame.K_DOWN]:

			self.rect_y += self.creative_speed

		if keys[pygame.K_RIGHT]:

			self.rect_x += self.creative_speed

		if keys[pygame.K_LEFT]:

			self.rect_x -= self.creative_speed

	def _update_sprites(self):

		if self.isWalk:

			if self.walkCount <= 5:
				if not self.isHoldingBabe:
					self.current_image = self.sprites[self.direction]["King_Walk1"]
				else:
					self.current_image = self.sprites["ending"][f"King_Walk1_{self.direction}"]

			elif self.walkCount <= 8:
				if not self.isHoldingBabe:
					self.current_image = self.sprites[self.direction]["King_MidWalk"]
				else:
					self.current_image = self.sprites["ending"][f"King_MidWalk_{self.direction}"]

			elif self.walkCount <= 13:
				if not self.isHoldingBabe:
					self.current_image = self.sprites[self.direction]["King_Walk2"]
				else:
					self.current_image = self.sprites["ending"][f"King_Walk2_{self.direction}"]

			elif self.walkCount <= 18:
				if not self.isHoldingBabe:
					self.current_image = self.sprites[self.direction]["King_MidWalk"]
				else:
					self.current_image = self.sprites["ending"][f"King_MidWalk_{self.direction}"]
			else:
				self.walkCount = 0

			self.walkCount += 1
		
		else:

			if self.isSplat:

				self.current_image = self.sprites[self.direction]["King_Fell"]

			elif self.isSnatch:

				self.current_image = self.sprites["ending"]["King_Snatch"]

			elif self.isDance:

				if self.danceCount <= 16:
					self.current_image = self.sprites[self.direction]["King_Dance_1"]

				elif self.danceCount <= 32:
					self.current_image = self.sprites[self.direction]["King_Dance_2"]

				elif self.danceCount <= 48:
					self.current_image = self.sprites[self.direction]["King_Dance_3"]

				elif self.danceCount <= 64:
					self.current_image = self.sprites[self.direction]["King_Dance_2"]

				else:
					self.danceCount = 0

				self.danceCount += 1

				if (self.idle_counter - self.idle_time) % self.idle_length == 0:
					self.isDance = False

			elif self.isLookUp:

				self.current_image = self.sprites[self.direction]["King_Look_Up"]

				if (self.idle_counter - self.idle_time) % self.idle_length == 0:
					self.isLookUp = False				

			elif self.idle_counter > self.idle_time and (self.idle_counter - self.idle_time) % self.idle_length == 0:

					x = random.randint(0, 2)

					if x == 0:

						self.isDance = True

					elif x == 1:

						self.isLookUp = True

					else:

						pass

			else:
				
				if self.isHoldingBabe:
					self.current_image = self.sprites["ending"][f"King_Hold_Babe_{self.direction}"]

				elif self.isSnatch:
					self.current_image = self.sprites["ending"]["King_Snatch"]

				elif self.isHoldingUpHands:
					self.current_image = self.sprites["ending"]["King_Hold_Up_Hands"]

				elif self.isWearingCrown:
					self.current_image = self.sprites["ending"]["King_Standing"]

				else:
					self.current_image = self.sprites[self.direction]["King_Standing"]

			self.walkCount = 0

		if self.isCrouch:

			if not self.isHoldingBabe:

				self.current_image = self.sprites[self.direction]["King_Crouch"]

			else:

				self.current_image = self.sprites["ending"]["King_Hold_Babe_Crouch"]

		if self.isFalling:

			if not self.collided:

				if self.angle <= math.pi/2 or self.angle >= 3 * math.pi / 2:

					if self.isHoldingBabe:

						self.current_image = self.sprites["ending"]["King_Umbrella1"]

					elif self.isWearingCrown:

						self.current_image = self.sprites["ending"]["King_Jump"]

					else:

						self.current_image = self.sprites[self.direction]["King_Jump"]


				else:

					if self.isHoldingBabe:

						if self.speed == self.maxSpeed:

							if self.umbrellaCount > 28:

								self.umbrellaCount = 11

							if self.umbrellaCount <= 10:

								self.current_image = self.sprites["ending"]["King_Umbrella0"]

							elif self.umbrellaCount <= 16:

								if self.isAdmiring:

									self.current_image = self.sprites["ending"]["King_Look_Up_Umbrella1"]

								else:

									self.current_image = self.sprites["ending"]["King_Normal_Umbrella1"]

							elif self.umbrellaCount <= 22:

								if self.isAdmiring:

									self.current_image = self.sprites["ending"]["King_Look_Up_Umbrella2"]

								else:

									self.current_image = self.sprites["ending"]["King_Normal_Umbrella2"]

							elif self.umbrellaCount <= 28:

								if self.isAdmiring:

									self.current_image = self.sprites["ending"]["King_Look_Up_Umbrella3"]

								else:

									self.current_image = self.sprites["ending"]["King_Normal_Umbrella3"]

							self.umbrellaCount += 1

						else:

							self.current_image = self.sprites["ending"]["King_Umbrella1"]

					elif self.isWearingCrown:

						self.current_image = self.sprites["ending"]["King_JumpFall"]	

					else:

						self.current_image = self.sprites[self.direction]["King_JumpFall"]

					
			else:
				self.current_image = self.sprites[self.direction]["King_CollisionFall"]

	def _update_audio1(self):

		if self.lastCollision:

			if self.isJump:

				self.channel.play(self.audio[self.lastCollision.type]["king_jump"])


	def _update_audio2(self):

		if self.lastCollision:

			if self.isFalling:

				if any([self.collideTop, self.collideLeft, self.collideRight]) and not self.isWalk:

					self.channel.play(self.audio[self.lastCollision.type]["king_bump"])

			if self.isLanded and not self.isSplat:

				self.channel.play(self.audio[self.lastCollision.type]["king_land"])

			elif self.isLanded and self.isSplat:

				self.channel.play(self.audio[self.lastCollision.type]["king_splat"])

	def _update_particles(self):

		if self.isJump:

			self.jump_particle.play((self.x, self.y, self.width, self.height))

			self.isJump = False

		if self.isLanded:

			if self.lastCollision.type == "Snow":
			
				self.snow_jump_particle.play((self.x, self.y, self.width, self.height))

			self.isLanded = False

	def _update_timer(self):

		if not self.timer.start_time:

			self.timer.start()

		self.time += self.timer.elapsed_time()

	def _update_stats(self):

		os.environ["TIME"] = str(self.time)
		os.environ["JUMPS"] = str(self.jumps)
		os.environ["FALLS"]  = str(self.falls)


	def reset(self):

		self.isWalk = False

		self.isCrouch = False

		self.isFalling = False

		self.isContact = False

		# self.isSplat = True
		self.isSplat = False

		self.isDance = False

		self.isLookUp = False

		self.isSnatch = False

		self.isHoldingUpHands = False

		self.isHoldingBabe = False

		self.isAdmiring = False

		self.isWearingCrown = False

		self.collided = False

		self.jumpParticle = False

		self.lastCollision = None

		self.collideTop = False

		self.collideRight = False

		self.collideLeft = False

		self.collideBottom = False

		self.collideRamp = False

		self.isJump = False

		self.isLanded = False

		# Stats

		self.time = 0

		self.jumps = 0

		self.falls = 0

		# Animation

		self.x, self.y = 230, 298

		self.width, self.height = 32, 32

		self.rect_x, self.rect_y = self.x + 1, self.y + 7

		self.rect_width, self.rect_height = self.width - 12, self.height - 8

		self.direction = "right"

		self.danceCount = 0

		self.walkCount = 0

		self.jumpCount = 0

		self.umbrellaCount = 0

		self.idle_counter = 0

		self.speed, self.angle = 0, 0

		self._update_sprites()

