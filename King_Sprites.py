#!/usr/bin/env python
#
#
#
#

import pygame
import math
import collections
import os
from spritesheet import SpriteSheet

class King_Sprites():

	def __init__(self):

		self.filename = "images\\sheets\\base.png"

		self.filename2 = "images\\sheets\\ending_animations.png"

		self.spritesheet = SpriteSheet(self.filename)

		self.spritesheet2 = SpriteSheet(self.filename2)

		self.start_rect, self.start_rect2, self.start_rect3, self.start_rect4, self.start_rect5, self.start_rect6, self.start_rect7 = (224, 8, 32, 40), (64, 0, 32, 32), (96, 64, 32, 32), (0, 28, 32, 36), (0, 96, 96, 96), (224, 128, 40, 32),(192, 192, 96, 96) 

		self.sprite_names = ["King_Standing",
								"King_Walk1",
								"King_MidWalk",
								"King_Walk2",
								"King_Crouch",
								"King_Jump",
								"King_JumpFall",
								"King_Fell",
								"King_CollisionFall",
								"King_Dance_1",
								"King_Dance_2",
								"King_Dance_3",
								"King_Look_Up"]

		self.ending_sprite_names = ["King_Hold_Up_Hands",
									"King_Standing",
									"King_Look_Up",
									"King_Hold_Babe_left",
									"King_Hold_Babe_right",
									"King_Hold_Babe_Crouch",
									"King_Walk1_left",
									"King_MidWalk_left",
									"King_Walk2_left",
									"King_Walk1_right",
									"King_MidWalk_right",
									"King_Walk2_right",
									"King_JumpFall",
									"King_Jump",
									"King_Umbrella0",
									"King_Umbrella1",
									"King_Normal_Umbrella1",
									"King_Normal_Umbrella2",
									"King_Look_Up_Umbrella1",
									"King_Look_Up_Umbrella2",
									"King_Snatch",
									"King_Normal_Umbrella3",
									"King_Look_Up_Umbrella3"]


		# self.hitbox_offsets = [(1, 4, -6, -4),
		# 						(1, 4, -6, -4),
		# 						(1, 4, -6, -4),
		# 						(1, 4, -6, -4),
		# 						(1, 4, -6, -4),
		# 						(1, 4, -6, -4),
		# 						(1, 4, -6, -4),
		# 						(1, 4, -6, -4),
		# 						(1, 4, -6, -4),
		# 						(1, 4, -6, -4),
		# 						(1, 4, -6, -4),
		# 						(1, 4, -6, -4),
		# 						(1, 4, -6, -4)]

		# self.hitbox_offsets = [tuple(map(lambda x: x * self.scale, t)) for t in self.hitbox_offsets]

		# self.mirrored_hitbox_offsets = [(1, 4, -6, -4),
		# 								(1, 4, -6, -4),
		# 								(1, 4, -6, -4),
		# 								(1, 4, -6, -4),
		# 								(1, 4, -6, -4),
		# 								(1, 4, -6, -4),
		# 								(1, 4, -6, -4),
		# 								(1, 4, -6, -4),
		# 								(1, 4, -6, -4),
		# 								(1, 4, -6, -4),
		# 								(1, 4, -6, -4),
		# 								(1, 4, -6, -4),
		# 								(1, 4, -6, -4)]

		# self.mirrored_hitbox_offsets = [tuple(map(lambda x: x * self.scale, t)) for t in self.mirrored_hitbox_offsets]

		self.king_images = collections.defaultdict()

		self._load_images()

	def _load_images(self):

		images = self.spritesheet.load_grid(self.start_rect, 4, 3, -1) + [self.spritesheet.image_at((224, 128, 32, 40), -1)]

		ending_images = self.spritesheet2.load_grid(self.start_rect2, 3, 2, -1) + self.spritesheet2.load_grid(self.start_rect3, 6, 1, -1) + self.spritesheet2.load_grid(self.start_rect4, 2, 1, -1) + self.spritesheet2.load_grid(self.start_rect5, 2, 3, -1) + [self.spritesheet2.image_at(self.start_rect6, -1)] + self.spritesheet2.load_grid(self.start_rect7, 1, 2, -1)
		
		mirrored_images = [pygame.transform.flip(image, True, False) for image in images]

		self.king_images["right"] = dict(zip(self.sprite_names, images))

		self.king_images["left"] = dict(zip(self.sprite_names, mirrored_images))

		self.king_images["ending"] = dict(zip(self.ending_sprite_names, ending_images))

if __name__ == "__main__":

	pygame.init()

	screen = pygame.display.set_mode((400, 400))

	sprites = King_Sprites()

	run = True

	while run:

		for event in pygame.event.get():

			if event.type == pygame.QUIT:

				run = False

		screen.fill((0, 0, 0))

		screen.blit(sprites.king_images["right"]["King_Standing"], (0, 0))

		pygame.display.flip()







