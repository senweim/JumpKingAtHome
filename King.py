#!/usr/bin/env python
#
#
#
#

import pygame
import math
import collections
from physics import add_vectors
from spritesheet import SpriteSheet

class King(pygame.sprite.Sprite):

	""" Represents the King """

	def __init__(self, jk_game):

		""" Initialize attributes to represent the King """
		super().__init__()

		self.sprites = self._load_sprites()
		self.image = self.sprites["right"]["King_Fell"]
		self.screen = jk_game

		# Movement 

		self.x, self.y = 175, 298
		self.width, self.height = 32, 32

		self.x_velocity = 0
		self.y_velocity = 0
		self.angle = 0
		self.speed = 0
		self.gravity_constant = (math.pi, 1)
		self.elasticity = 0.5

		self.walking = False
		self.walkCount = 0
		self.walking_angle = math.pi/2
		self.walking_speeds = {"left":-5, "right":5}

		self.facing = "right"

		self.crouching = False
		self.collided = False
		self.direction_angles = {'up' : 0, 'left' : -math.pi/3, 'right' : math.pi/3}
		self.jump_timer = 0

	# IMAGING
	def update(self, platforms):
		
		self.move()

		self.bounce_back(platforms)
		
		self.update_walking_animation()

		self.update_jumping_animation()

	def update_walking_animation(self):

		if self.walking:		
			if self.walkCount <= 7:
				self.image = self.sprites[self.facing]["King_Walk1"]

			elif self.walkCount <= 10:
				self.image = self.sprites[self.facing]["King_MidWalk"]

			elif self.walkCount <= 17:
				self.image = self.sprites[self.facing]["King_Walk2"]

			elif self.walkCount <= 20:
				self.image = self.sprites[self.facing]["King_MidWalk"]
			
			else:
				self.walkCount = 0
		
		else:
			self.image = self.sprites[self.facing]["King_Standing"]


	def update_jumping_animation(self):

		if self.crouching:
			self.image = self.sprites[self.facing]["King_Crouch"]

		if self.falling:
			if not self.collided:
				if abs(self.angle) <= math.pi/2:
					self.image = self.sprites[self.facing]["King_Jump"]
				else:
					self.image = self.sprites[self.facing]["King_JumpFall"]
			else:
				self.image = self.sprites[self.facing]["King_CollisionFall"]

	def blitme(self):

		"""Draw the piece at its current location."""
		
		self.screen.blit(self.image, (self.x, self.y))
		#pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 1)

	def _load_sprites(self):

		""" Builds the overall set:
		- Loads images from the sprite sheet.
		- Adds each sprite to the group self.sprites
		"""

		filename = 'base2.png'

		# Sprite Names

		king_sprites = ["King_Standing",
						"King_Walk1",
						"King_MidWalk",
						"King_Walk2",
						"King_Crouch",
						"King_Jump",
						"King_JumpFall",
						"King_Fell",
						"King_CollisionFall"]


		king_spritesheet = SpriteSheet(filename)

		king_rect = (50, 8, 32, 32)

		load_images = king_spritesheet.load_strip(king_rect, 9, -1)

		king_images = collections.defaultdict()
		
		king_images["right"] = dict(zip(king_sprites, load_images))

		king_images["left"] = dict(zip(king_sprites, [pygame.transform.flip(image, True, False) for image in load_images]))

		return king_images

	# MOVEMENT

	@property
	def rect(self):
		return pygame.Rect((self.x, self.y, 32, 32))

	@property
	def falling(self):
		return self.speed != 0
	
	@property
	def time_lapsed(self):
		return pygame.time.get_ticks() - self.jump_timer
	
	
	def walk(self):

		self.angle = math.pi/2
		self.speed = self.walking_speeds[self.facing]
		self.walking = True
		self.walkCount += 1

	def walk_stop(self):

		self.angle = 0
		self.speed = 0
		self.walking = False
		self.walkCount = 0

	def crouch(self):

		self.crouching = True
		self.walking = False

		self.jump_timer = pygame.time.get_ticks()

	def jump(self, time, direction):

		self.angle = self.direction_angles[direction] * (1 - time / 1400)
		self.speed = 7 + time / 50
		self.jump_timer = 0

		self.crouching = False
		self.walking = False

	def bounce_back(self, platforms):

		for platform in platforms:

			if self.rect.colliderect(platform):

				if self.rect.bottom > platform.top and self.rect.bottom - platform.top <= self.speed and abs(self.angle) > math.pi/2:
					self.angle = 0
					self.speed = 0
					self.y = platform.top - self.height

				elif self.rect.top < platform.bottom and platform.bottom - self.rect.top <= self.speed and abs(self.angle) < math.pi/2:
					self.y = platform.bottom
					self.angle = math.pi - self.angle
					self.speed *= self.elasticity
					self.collided = True

				elif self.rect.left < platform.right and platform.right - self.rect.left <= self.speed:
					self.x = platform.right
					self.angle = - self.angle
					self.speed *= self.elasticity
					self.facing = "left"
					self.collided = True

				elif self.rect.right > platform.left and self.rect.right - platform.left <= self.speed:
					self.x = platform.left - self.width
					self.angle = - self.angle
					self.speed *= self.elasticity
					self.facing = "right"
					self.collided = True

		if self.rect.bottom > self.screen.get_height():
			self.angle = 0
			self.speed = 0
			self.y = self.screen.get_height() - self.height

		if self.rect.right > self.screen.get_width():
			self.x = self.screen.get_width() - self.width
			self.angle = - self.angle
			self.speed *= self.elasticity
			self.facing = "right"
			self.collided = True

		if self.rect.left < 0:
			self.x = 0
			self.angle = - self.angle
			self.speed *= self.elasticity
			self.facing = "left"
			self.collided = True

		if not self.falling:
			self.collided = False
		
	def move(self):

		if self.falling:
			self.angle, self.speed = add_vectors(self.angle, self.speed, self.gravity_constant[0], self.gravity_constant[1])
		
		self.x += math.sin(self.angle) * self.speed
		self.y -= math.cos(self.angle) * self.speed

	# Controls
	def check_controls(self):

		keys = pygame.key.get_pressed()

		jump_direction = "up"

		if not self.falling:

			if keys[pygame.K_RIGHT]:
				self.facing = "right"
				jump_direction = "right"
				if not self.crouching:
					self.walk()

			elif keys[pygame.K_LEFT]:
				self.facing = "left"
				jump_direction = "left"
				if not self.crouching:
					self.walk()
			else:
				self.walk_stop()

			if keys[pygame.K_SPACE]:

				if not self.crouching:
					self.crouch()

				if self.time_lapsed > 700:
					self.jump(self.time_lapsed, jump_direction)

			elif self.crouching:
				self.jump(self.time_lapsed, jump_direction)







