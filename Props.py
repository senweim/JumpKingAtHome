#!/usr/bin/env python
#
#
#
#

import pygame
import collections
import math
import os
import random
from spritesheet import SpriteSheet

class Props:

	def __init__(self):

		self.Bonfire = Bonfire()

		self.FlowingWater = FlowingWater()

		self.SewerDrop = SewerDrop()

		self.OvenFire = OvenFire()

		self.Kettle = Kettle()

		self.Grammofon = Grammofon()

		self.Merchant = Merchant()

		self.Gargoyles = [Gargoyle(276, 189), Gargoyle(330, 95, True), Gargoyle(385, 225, True), Gargoyle(422, 181, True)]

		self.Candles = [Candle(305, 287), Candle(92, 135), Candle(100, 135),
						Candle(96, 143), Candle(117, 135), Candle(125, 135), 
						Candle(121, 143), Candle(125, 225), Candle(139, 225), 
						Candle(160, 225), Candle(173, 225), Candle(131, 243), 
						Candle(140, 243), Candle(159, 243), Candle(167, 243), 
						Candle(165, 120), Candle(173, 120), Candle(169, 127), 
						Candle(190, 120), Candle(197, 120), Candle(194, 127), 
						Candle(212, 215), Candle(220, 215), Candle(216, 221), 
						Candle(237, 215), Candle(245, 215), Candle(241, 221), 
						Candle(267, 152), Candle(276, 153), Candle(272, 159), 
						Candle(294, 153), Candle(302, 153), Candle(298, 160), 
						Candle(388, 80), Candle(396, 80), Candle(392, 86), 
						Candle(413, 80), Candle(421, 80), Candle(417, 86), 
						Candle(293, 56), Candle(300, 56), Candle(297, 62), 
						Candle(316, 56), Candle(324, 56), Candle(320, 63), 
						Candle(333, 0), Candle(341, 0), Candle(337, 7), 
						Candle(357, 0), Candle(364, 0), Candle(361, 7), 
						Candle(110, 0), Candle(116, 0), Candle(113, 6), 
						Candle(133, 0), Candle(141, 0), Candle(137, 7), 
						Candle(62, 184), Candle(71, 184), Candle(67, 190), 
						Candle(84, 184), Candle(94, 184), Candle(89, 190), 
						Candle(133, 184), Candle(125, 184), Candle(129, 189), 
						Candle(154, 184), Candle(145, 184), Candle(149, 190), 
						Candle(89, 215), Candle(100, 215), Candle(118, 215), 
						Candle(131, 215), Candle(92, 233), Candle(98, 233), 
						Candle(119, 232), Candle(126, 232), Candle(136, 265), 
						Candle(142, 265), Candle(139, 270), Candle(156, 265), 
						Candle(164, 265), Candle(160, 271), Candle(207, 265), 
						Candle(198, 265), Candle(203, 271), Candle(218, 266), 
						Candle(225, 266), Candle(222, 273), Candle(161, 295),
						Candle(172, 295), Candle(190, 296), Candle(204, 296), 
						Candle(164, 312), Candle(172, 312), Candle(189, 313), 
						Candle(197, 313), Candle(110, 325), Candle(117, 325), 
						Candle(113, 331), Candle(133, 325), Candle(140, 325), 
						Candle(137, 330), Candle(333, 325), Candle(341, 325), 
						Candle(337, 330), Candle(356, 325), Candle(364, 325), 
						Candle(360, 330), Candle(215, 120), Candle(224, 120), 
						Candle(220, 126), Candle(237, 120), Candle(246, 121), 
						Candle(241, 126), Candle(276, 120), Candle(285, 120), 
						Candle(281, 125), Candle(296, 121), Candle(306, 120), 
						Candle(302, 125), Candle(237, 152), Candle(252, 152), 
						Candle(271, 152), Candle(286, 152), Candle(252, 169), 
						Candle(243, 169), Candle(273, 170), Candle(281, 169), 
						Candle(318, 175), Candle(328, 175), Candle(323, 183), 
						Candle(340, 177), Candle(349, 177), Candle(345, 182), 
						Candle(380, 176), Candle(389, 176), Candle(385, 181), 
						Candle(402, 176), Candle(410, 176), Candle(406, 182), 
						Candle(341, 207), Candle(356, 208), Candle(375, 208), 
						Candle(389, 208), Candle(348, 225), Candle(355, 225), 
						Candle(377, 225), Candle(384, 225), Candle(135, 81), 
						Candle(145, 80), Candle(140, 86), Candle(157, 81), 
						Candle(165, 81), Candle(161, 86), Candle(157, 112), 
						Candle(171, 112), Candle(189, 112), Candle(204, 111), 
						Candle(163, 130), Candle(170, 130), Candle(191, 130), 
						Candle(200, 130), Candle(195, 80), Candle(202, 80), 
						Candle(199, 85), Candle(216, 81), Candle(225, 81), 
						Candle(221, 87), Candle(242, 144), Candle(253, 144), 
						Candle(248, 150), Candle(262, 145), Candle(270, 145), 
						Candle(267, 153), Candle(300, 145), Candle(309, 145), 
						Candle(305, 150), Candle(321, 145), Candle(330, 146), 
						Candle(326, 150), Candle(260, 176), Candle(275, 176), 
						Candle(293, 176), Candle(308, 176), Candle(268, 193), 
						Candle(274, 193), Candle(295, 193), Candle(302, 193)]

		self.DungeonTorches = [DungeonTorch(160, 62), DungeonTorch(255, 195), DungeonTorch(162, 125), 
								DungeonTorch(254, 12), DungeonTorch(275, 184), DungeonTorch(288, 196), 
								DungeonTorch(295, 184), DungeonTorch(315, 184), DungeonTorch(304, 196)]

		self.Flags = [Flag(213, 105, True), Flag(97, 57), Flag(242, 88)]

		self.Dust1 = [Dust1(133, 111), Dust1(346, 208), Dust1(109, 144), Dust1(130 ,40), Dust1(240, 312), Dust1(180, 176), Dust1(268, 264)]

		self.Dust2 = [Dust2(144, 111), Dust2(328, 160), Dust2(343, 160), Dust2(349, 96), Dust2(96, 16), Dust2(116, 40), Dust2(168, 176), Dust2(155, 264)]

		self.Dust3 = [Dust3(380, 16), Dust3(318, 287), Dust3(260, 136), Dust3(131, 56), Dust3(343, 168), Dust3(280, 264)]

		self.props = collections.defaultdict()

		self._load_props()

	def _load_props(self):

		self.props[0] = [self.Bonfire, self.FlowingWater]

		self.props[6] = [self.SewerDrop, self.Candles[0]]

		self.props[9] = [self.OvenFire, self.Kettle, self.DungeonTorches[0]]

		self.props[10] = [*self.DungeonTorches[1:4]]

		self.props[11] = [*self.DungeonTorches[4:9]]

		self.props[14] = [self.Grammofon, self.Merchant]

		self.props[21] = [self.Flags[0]]

		self.props[24] = [*self.Flags[1:3]]

		self.props[26] = [self.Gargoyles[3]]

		self.props[28] = [*self.Gargoyles[0:3]]

		self.props[32] = [*self.Candles[1:57]] 

		self.props[33] = [*self.Candles[57:149]]

		self.props[34] = [*self.Candles[149:202]]

		self.props[39] = [self.Dust1[0], *self.Dust2[0:3], *self.Dust3[0:2]]

		self.props[40] = [*self.Dust1[1:3], *self.Dust2[3:5], *self.Dust3[2:4]]

		self.props[41] = [*self.Dust1[3:6], *self.Dust2[5:7], self.Dust3[4]]

		self.props[42] = [self.Dust1[6], self.Dust2[7], self.Dust3[5]]

class Prop:

	def __init__(self):

		self.images = None

		self.interval = 10

		self.blit_counter = 0

	@property
	def rect(self):
		return pygame.Rect(self.x, self.y, self.width, self.height)
	

	def blitme(self, screen):

		if self.blit_counter >= len(self.images) * self.interval:
			self.blit_counter = 0

		screen.blit(self.images[self.blit_counter // self.interval], self.rect)

		self.blit_counter += 1

class Gargoyle(Prop):

	def __init__(self, x, y, reverse = False):

		super().__init__()

		self.filename = "props\\gargoyle.png"

		self.start_rect = (0, 0, 41, 39)

		self.x, self.y, self.width, self.height = x, y, 41, 32

		self.spritesheet = SpriteSheet(self.filename)

		self.interval = random.randint(100, 200)

		self.images = self.spritesheet.load_grid(self.start_rect, 2, 1, -1)

		if reverse:

			self.images = [pygame.transform.flip(image, True, False) for image in self.images]

class Merchant(Prop):

	def __init__(self):

		super().__init__()

		self.filename = "props\\merchant.png"

		self.start_rect = (0, 0, 32, 32)

		self.x, self.y, self.width, self.height = 30, 270, 32, 32

		self.spritesheet = SpriteSheet(self.filename)

		self.interval = 60

		self.images = self.spritesheet.load_grid(self.start_rect, 2, 2, -1)

class Bonfire(Prop):

	def __init__(self):

		super().__init__()

		self.filename = "props\\Bonfire.png"

		self.spritesheet = SpriteSheet(self.filename)

		self.start_rect = (0, 0, 32, 32)

		self.x, self.y, self.width, self.height = 160, 298, 32, 32

		self.interval = 5

		self.images = self.spritesheet.load_strip(self.start_rect, 3, -1)

	def blitme(self, screen):

		if self.blit_counter >= len(self.images) * self.interval:
			self.blit_counter = 0

		screen.blit(self.images[self.blit_counter // self.interval], self.rect, special_flags = pygame.BLEND_RGBA_ADD)

		self.blit_counter += 1

class FlowingWater(Prop):

	def __init__(self):

		super().__init__()

		self.filename = "props\\1_water.png"

		self.spritesheet = SpriteSheet(self.filename)

		self.start_rect = (0, 0, 442, 75)

		self.x, self.y, self.width, self.height = 0, 283, 442, 75

		self.interval = 10

		self.images = self.spritesheet.load_column(self.start_rect, 2, -1)

class SewerDrop(Prop):

	def __init__(self):

		super().__init__()

		self.filename = "props\\SewerDrop.png"

		self.spritesheet = SpriteSheet(self.filename)

		self.start_rect = (0, 0, 16, 48)

		self.x, self.y, self.width, self.height = 340, 160, 16, 48

		self.interval = 6

		self.images = self.spritesheet.load_strip(self.start_rect, 10, -1)

class OvenFire(Prop):

	def __init__(self):

		super().__init__()

		self.filename = "props\\ovenfire.png"

		self.spritesheet = SpriteSheet(self.filename)

		self.start_rect = (0, 0, 32, 32)

		self.x, self.y, self.width, self.height = 400, 82, 32, 32

		self.interval = 6

		self.images = self.spritesheet.load_strip(self.start_rect, 3, -1)

class Kettle(Prop):

	def __init__(self):

		super().__init__()

		self.filename = "props\\kettle.png"

		self.spritesheet = SpriteSheet(self.filename)

		self.start_rect = (0, 0, 28, 24)

		self.x, self.y, self.width, self.height = 442, 64, 28, 24

		self.interval = 6

		self.images = self.spritesheet.load_strip(self.start_rect, 3, -1)

class Grammofon(Prop):

	def __init__(self):

		super().__init__()

		self.filename = "props\\grammofon.png"

		self.spritesheet = SpriteSheet(self.filename)

		self.start_rect = (0, 0, 15, 25)

		self.x, self.y, self.width, self.height = 10, 278, 15, 25

		self.interval = 6

		self.images = self.spritesheet.load_strip(self.start_rect, 2, -1)

class Candle(Prop):

	def __init__(self, x, y):

		super().__init__()

		self.filename = "props\\Candle.png"

		self.spritesheet = SpriteSheet(self.filename)

		self.start_rect = (0, 0, 14, 18)

		self.x, self.y, self.width, self.height = x, y, 14, 18

		self.interval = 6

		self.images = self.spritesheet.load_grid(self.start_rect, 2, 2, -1)

	def blitme(self, screen):

		if self.blit_counter == self.interval * len(self.images):

			self.blit_counter = 0

		screen.blit(self.images[self.blit_counter//self.interval], self.rect, special_flags = pygame.BLEND_RGBA_ADD)

		self.blit_counter += 1

class DungeonTorch(Prop):
	
	def __init__(self, x, y):

		super().__init__()

		self.filename = "props\\DungeonTorch.png"

		self.spritesheet = SpriteSheet(self.filename)

		self.start_rect = (0, 0, 32, 32)

		self.x, self.y, self.width, self.height = x, y, 32, 32

		self.interval = 6

		self.images = self.spritesheet.load_grid(self.start_rect, 2, 2, -1)

	def blitme(self, screen):

		if self.blit_counter == self.interval * len(self.images):

			self.blit_counter = 0

		screen.blit(self.images[self.blit_counter//self.interval], self.rect, special_flags = pygame.BLEND_RGBA_ADD)

		self.blit_counter += 1

class Flag(Prop):

	def __init__(self, x, y, reverse = False):

		super().__init__()

		self.filename = "props\\Flag.png"

		self.spritesheet = SpriteSheet(self.filename)

		self.start_rect = (0, 0, 96, 32)

		self.x, self.y, self.width, self.height = x, y, 96, 32

		self.interval = 6

		self.images = self.spritesheet.load_grid(self.start_rect, 2, 5, -1)

		if reverse:

			self.images = [pygame.transform.flip(image, True, False) for image in self.images]

class Dust1(Prop):

	def __init__(self, x, y):

		super().__init__()

		self.filename = "props\\dust1.png"

		self.spritesheet = SpriteSheet(self.filename)

		self.start_rect = (0, 0, 6, 62)

		self.x, self.y, self.width, self.height = x, y, 6, 62

		self.interval = 6

		self.frequency = 2000

		self.images = self.spritesheet.load_strip(self.start_rect, 15, -1)

	def blitme(self, screen):
		
		if random.randint(0, self.frequency) < 10 or self.blit_counter > 1:

			if self.blit_counter == 90:

				self.blit_counter = 0

			screen.blit(self.images[self.blit_counter//self.interval], self.rect)

			self.blit_counter += 1

class Dust2(Prop):

	def __init__(self, x, y):

		super().__init__()

		self.filename = "props\\dust2.png"

		self.spritesheet = SpriteSheet(self.filename)

		self.start_rect = (0, 0, 9, 61)

		self.x, self.y, self.width, self.height = x, y, 9, 61

		self.interval = 6

		self.frequency = 2000

		self.images = self.spritesheet.load_strip(self.start_rect, 15, -1)

	def blitme(self, screen):

		if random.randint(0, self.frequency) < 10 or self.blit_counter > 1:

			if self.blit_counter == self.interval * len(self.images):

				self.blit_counter = 0

			screen.blit(self.images[self.blit_counter//self.interval], self.rect)

			self.blit_counter += 1

class Dust3(Prop):

	def __init__(self, x, y):

		super().__init__()

		self.filename = "props\\dust3.png"

		self.spritesheet = SpriteSheet(self.filename)

		self.start_rect = (0, 0, 5, 61)

		self.x, self.y, self.width, self.height = x, y, 5, 61

		self.interval = 6

		self.frequency = 2000

		self.images = self.spritesheet.load_strip(self.start_rect, 25, -1)

	def blitme(self, screen):

		if random.randint(0, self.frequency) < 10 or self.blit_counter > 1:

			if self.blit_counter >= self.interval * len(self.images):

				self.blit_counter = 0

			screen.blit(self.images[self.blit_counter//self.interval], self.rect)

			self.blit_counter += 1

if __name__ == "__main__":

	Props()