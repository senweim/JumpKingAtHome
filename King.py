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

class King():

	""" represents the king """

	def __init__(self, screen, levels):

		# Static 

		self.screen = screen

		self.scale = int(os.environ.get("resolution"))

		self.sprites = King_Sprites().king_images

		self.levels = levels

		self.timer = Timer()

		self.creative_speed = 10 * self.scale

		self.walkAngles = {"right" : math.pi/2, "left" : -math.pi/2}

		self.jumpAngles = {'up' : 0, 'left' : -math.pi/3.5, 'right' : math.pi/3.5}

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

		# Animation

		self.x, self.y = 230 * self.scale, 298 * self.scale

		self.width, self.height = 32 * self.scale, 32 * self.scale

		self.rect = pygame.Rect((self.x + self.scale, self.y + 7 * self.scale, self.width - 12 * self.scale, self.height - 8 * self.scale))

		self.direction = "right"

		self.danceCount = 0

		self.walkCount = 0

		self.umbrellaCount = 0

		self.maxSpeed = 11 * self.scale
 
		self.idle_counter = 0

		self.idle_time = 300

		self.idle_length = 200

		self.current_image = self.sprites[self.direction]["King_Fell"]

		self.mask = pygame.mask.from_surface(self.current_image)

		# Particles

		self.jump_particle = King_Particle("jump_particle.png", 5, 1, 32)

		self.snow_jump_particle = King_Particle("snow_jump_particle.png", 4, 3, 36)

		self.level_change = 0

		self.isJump = False
		self.isLanded = False

		# Audio

		self.channel = pygame.mixer.Channel(4)

		self.audio = King_Audio().audio

		# Physics

		self.physics = Physics()

		self.speed, self.angle = 0, 0

		self.elasticity = 0.8

		self.charge_time = 0

	def blitme(self):

		self.screen.blit(self.current_image, (self.x, self.y))
		# pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 1)

		if not self.level_change:

			self.jump_particle.blitme(self.screen)

			self.snow_jump_particle.blitme(self.screen)

		else:

			self.jump_particle.reset()

			self.snow_jump_particle.reset()


	def update(self, command = None):

		if os.environ.get("mode") == "normal":

			if not self.isFalling and not self.levels.ending:

				self._check_events()

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

		else:

			self._creative()

			self._check_level()

			self._update_sprites()

	def _robot_check_events(self, command):

		if command:

			if command == "Crouch":

				self.isCrouch = True
				self.timer.start()

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

	def _check_events(self):

			keys = pygame.key.get_pressed()

			if keys[pygame.K_SPACE]:

				self.idle_counter = 0

				if not self.isCrouch:

					self.timer.start()

					self.isCrouch = True

				elif self.timer.elapsed_time() > 700:

					if keys[pygame.K_RIGHT]:

						self._jump("right")

					elif keys[pygame.K_LEFT]:

						self._jump("left")
					else:
						self._jump("up")

			else:

				if keys[pygame.K_RIGHT]:

					self.idle_counter = 0

					# Walk
					if not self.isCrouch:
						self._walk("right")
					# Jump
					else:
						self._jump("right")

				elif keys[pygame.K_LEFT]:

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

	def _add_gravity(self):

		self.angle, self.speed = self.physics.add_vectors(self.angle, self.speed, self.physics.gravity[0], self.physics.gravity[1])

	def _move(self):

		if self.speed > self.maxSpeed:
			self.speed = self.maxSpeed

		x, y = self.rect.x, self.rect.y

		self.rect.move_ip(round(math.sin(self.angle) * self.speed), round(-math.cos(self.angle) * self.speed))

		if self.rect.x != x or abs(self.rect.y - y) > 1:

			self.idle_counter = 0
			self.isLookUp = False
			self.isDance = False
			self.danceCount = 0

	def _collide_rect(self, rect1, rect2):

		return pygame.Rect(rect1[0], rect1[1], rect1[2], rect1[3] + 1).colliderect(rect2)

	def _check_collisions(self):

		self.isFalling = True

		self.collideTop = False
		self.collideRight = False
		self.collideLeft = False
		self.collideBottom = False
		self.collideRamp = False
		self.slip = 0
		self.slope = 0

		#print("------------------------------")

		for platform in self.levels.levels[self.levels.current_level].platforms:

			if self._collide_rect(self.rect, platform):
				#print(platform)
				if platform.slope:
 					
					if platform.slope[0] > 0:

						if platform.slope[1] > 0:

							rel_x = self.rect.right - platform.left

							if self.rect.top <= platform.bottom and round(platform.bottom - self.rect.top) <= round(self.speed) and abs(self.angle) < math.pi/2:
								self.rect.top = platform.bottom
								self.lastCollision = platform
								self.collideTop = True

							elif self.rect.left <= platform.right and round(platform.right - self.rect.left) <= round(self.speed) and self.rect.bottom > platform.top:
								self.rect.left = platform.right
								self.lastCollision = platform
								self.collided = True
								self.collideRight = True

							elif self.rect.right > platform.left and round(self.rect.right - platform.left) <= round(self.speed) and self.lastCollision != platform and math.sin(self.angle) > 0 and self.rect.bottom > platform.bottom:
								self.rect.right = platform.left
								self.collided = True
								self.lastCollision = platform
								self.collideLeft = True


							elif self.rect.bottom >= platform.top and round(self.rect.bottom - platform.top) <= round(self.speed) and self.rect.right > platform.right:
								self.rect.bottom = platform.top
								self.lastCollision = platform							
								self.collideRamp = True
								self.slope = platform.slope[0]
								self.slip = platform.slip

							elif self.rect.bottom >= round(platform.bottom - platform.slope[0] * rel_x):
								while self.rect.bottom >= round(platform.bottom - platform.slope[0] * rel_x):
									if self.isFalling:
										self.rect.move_ip(-1, -1)
									else:
										self.rect.move_ip(-1, 0)
									rel_x = self.rect.right - platform.left
								self.lastCollision = platform
								self.collideRamp = True
								self.slope = platform.slope[0]
								self.slip = platform.slip

						if platform.slope[1] < 0:

							rel_x = self.rect.left - platform.left

							if self.rect.bottom >= platform.top and round(self.rect.bottom - platform.top) <= round(self.speed) and abs(self.angle) > math.pi/2:
								self.slip += platform.slip 
								self.rect.bottom = platform.top
								self.isFalling = False
								self.collided = False
								self.lastCollision = platform
								self.isContact = False
								self.collideBottom = True

							elif self.rect.right >= platform.left and round(self.rect.right - platform.left) <= round(self.speed):
								self.rect.right = platform.left
								self.collided = True
								self.lastCollision = platform
								self.collideLeft = True

							elif self.rect.left <= platform.right and round(platform.right - self.rect.left) <= round(self.speed) and self.lastCollision != platform and math.sin(self.angle) < 0 and self.rect.top < platform.top:
								self.rect.left = platform.right
								self.collided = True
								self.lastCollision = platform
								self.collideRight = True

							elif self.rect.top < round(platform.bottom - platform.slope[0] * rel_x):

								while self.rect.top < round(platform.bottom - platform.slope[0] * rel_x):
									self.rect.move_ip(1, 0)
									rel_x = self.rect.left - platform.left

								self.collided = True
								self.collideTop = True
								self.lastCollision = platform

					if platform.slope[0] < 0:

						if platform.slope[1] > 0:

							rel_x = platform.right - self.rect.left

							if self.rect.top <= platform.bottom and round(platform.bottom - self.rect.top) <= round(self.speed) and abs(self.angle) < math.pi/2:
								self.rect.top = platform.bottom
								self.lastCollision = platform
								self.collideTop = True

							elif self.rect.right >= platform.left and round(self.rect.right - platform.left) <= round(self.speed) and self.rect.bottom > platform.top:
								self.rect.right = platform.left
								self.collided = True
								self.lastCollision = platform
								self.collideLeft = True

							elif self.rect.left <= platform.right and round(platform.right - self.rect.left) <= round(self.speed) and self.lastCollision != platform and math.sin(self.angle) < 0 and self.rect.bottom > platform.bottom:
								self.rect.left = platform.right
								self.collided = True
								self.lastCollision = platform
								self.collideRight = True


							elif self.rect.bottom >= platform.top and round(self.rect.bottom - platform.top) <= round(self.speed) and self.rect.left < platform.left:
								self.rect.bottom = platform.top
								self.lastCollision = platform							
								self.collideRamp = True
								self.slope = platform.slope[0]
								self.slip = platform.slip

							elif self.rect.bottom > round(platform.bottom + platform.slope[0] * rel_x):
								while self.rect.bottom > round(platform.bottom + platform.slope[0] * rel_x):
									if self.isFalling:
										self.rect.move_ip(1, -1)
									else:
										self.rect.move_ip(1, 0)
									rel_x = platform.right - self.rect.left
								self.slope = platform.slope[0]
								self.slip = platform.slip
								self.collideRamp = True
								self.lastCollision = platform

						if platform.slope[1] < 0:

							rel_x = platform.right - self.rect.right

							if self.rect.bottom >= platform.top and round(self.rect.bottom - platform.top) <= round(self.speed) and abs(self.angle) > math.pi/2:
								self.slip = platform.slip 
								self.rect.bottom = platform.top
								self.isFalling = False
								self.collided = False
								self.lastCollision = platform
								self.isContact = False
								self.collideBottom = True

							elif self.rect.left <= platform.right and round(platform.right - self.rect.left) <= round(self.speed):
								self.rect.left = platform.right
								self.collided = True
								self.lastCollision = platform
								self.collideRight = True

							elif self.rect.right > platform.left and round(self.rect.right - platform.left) <= round(self.speed) and self.lastCollision != platform and math.sin(self.angle) > 0 and self.rect.top < platform.top:
								self.rect.right = platform.left
								self.collided = True
								self.lastCollision = platform
								self.collideLeft = True

							elif self.rect.top < round(platform.bottom + platform.slope[0] * rel_x):

								while self.rect.top < round(platform.bottom + platform.slope[0] * rel_x):
									self.rect.move_ip(-1, 0)
									rel_x = platform.right - self.rect.right

								self.collided = True
								self.lastCollision = platform
								self.collideTop = True

				else:

					if self.rect.bottom >= platform.top and round(self.rect.bottom - platform.top) <= round(self.speed) and -math.cos(self.angle) > 0 and not platform.support:
						self.slip = platform.slip 
						self.rect.bottom = platform.top
						self.isFalling = False
						self.collided = False
						self.isContact = False
						self.collideBottom = True

						if not self.lastCollision:
							self.isLanded = True
							if self.speed >= self.maxSpeed:
								self.isSplat = True

						self.lastCollision = platform
						self.level_change = 0

					elif self.rect.top <= platform.bottom and round(platform.bottom - self.rect.top) <= round(self.speed) and abs(self.angle) < math.pi/2:
						self.rect.top = platform.bottom
						self.lastCollision = platform
						self.collideTop = True

					elif self.rect.left <= platform.right and round(platform.right - self.rect.left) <= round(self.speed):
						self.rect.left = platform.right
						self.lastCollision = platform
						self.collided = True
						self.collideRight = True

					elif self.rect.right >= platform.left and round(self.rect.right - platform.left) <= round(self.speed):
						self.rect.right = platform.left
						self.lastCollision = platform
						self.collided = True
						self.collideLeft = True
		
		# Hits The Sides

		if self.rect.right > self.screen.get_width():

			self.rect.right = self.screen.get_width()
			self.x = self.rect.left
			self.collideRight = True
			self.collided = True

		if self.rect.left < 0:
			self.rect.left = 0
			self.x = self.rect.right - self.width
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
				self.speed -= 0.35 * self.scale

			else:
				self.speed -= 0.1 * self.scale

			if self.speed > 10:
				self.speed = 10

		if self.isFalling:

			if self.collideTop:
				self.angle = math.pi - self.angle
				self.speed *= self.elasticity

			if self.collideRight or self.collideLeft:
				self.angle = -self.angle
				self.speed *= self.elasticity

			self.isCrouch = False
			self.timer.end()

		if self.collideBottom:

			self.angle, self.speed = self.physics.add_vectors(self.angle, self.speed, -self.physics.gravity[0], -self.physics.gravity[1])

			self.speed *= self.slip

	def _check_level(self):

		if self.rect.bottom < 0 and self.levels.current_level < self.levels.max_level:

			self.rect.bottom += self.screen.get_height()
			self.levels.current_level += 1
			self.level_change += 1

		if self.rect.bottom > self.screen.get_height():

			self.rect.bottom -= self.screen.get_height()
			self.levels.current_level -= 1
			self.level_change -= 1

	def _walk(self, direction):

		if self.lastCollision:
			if not self.lastCollision.snow:

				self.speed = self.scale
				self.angle = self.walkAngles[direction]
				self.isWalk = True

		self.isSplat = False
		self.direction = direction

	def _jump(self, direction):

		speed = (2 + (self.timer.elapsed_time()*2) / 185) * self.scale

		if direction == "up":
			angle = 0
		else:
			angle = self.jumpAngles[direction] * (1 - self.timer.elapsed_time() / 1175)

		if direction != "up":
			self.direction = direction

		if self.lastCollision.snow:

			if speed > 2.5 * self.scale:
				self.angle, self.speed = self.physics.add_vectors(self.angle, self.speed, angle, speed)

		else:
			self.angle, self.speed = self.physics.add_vectors(self.angle, self.speed, angle, speed)

		self.isSplat = False
		self.isJump = True
		self.isCrouch = False
		self.isWalk = False
		self.timer.end()

	def _creative(self):

		keys = pygame.key.get_pressed()

		if keys[pygame.K_UP]:

			self.rect.y -= self.creative_speed

		if keys[pygame.K_DOWN]:

			self.rect.y += self.creative_speed

		if keys[pygame.K_RIGHT]:

			self.rect.x += self.creative_speed

		if keys[pygame.K_LEFT]:

			self.rect.x -= self.creative_speed

	def _update_sprites(self):

		self.x = self.rect.x - 5 * self.scale
		self.y = self.rect.y - 9 * self.scale

		if self.direction == "left":
			self.x -= self.scale

		if self.isFalling:

			self.y += 4 * self.scale

			if self.isHoldingBabe:

				self.x -= 30 * self.scale
				self.y -= 30 * self.scale

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






