#!/usr/bin/env python
#
#
#
#

import pygame
import collections
import os

class Rectangles:

	def __init__(self):

		self.scale = int(os.environ.get("resolution"))

		self.levels = collections.defaultdict()

		self.levels[0]	=	[(352, 185, 128, 175, 0, 0, False, False),
							(185, 40, 110, 50, 0, 0, False, False),
							(128, 330, 224, 30, 0, 0, False, False),
							(8, 184, 120, 107, 0, 0, False, False),
							(8, 291, 65, 69, 0, 0, False, False),
							(73, 330, 55, 30, 0, 0, False, False),
							(0, 0, 8, 360, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False)]

		self.levels[1]	=	[(296, 296, 95, 38, 0, 0, False, False),
							(409, 197, 71, 35, 0, 0, False, False),
							(255, 199, 74, 33, 0, 0, False, False),
							(119, 103, 74, 65, 0, 0, False, False),
							(0, 80, 81, 86, 0, 0, False, False),
							(0, 0, 8, 360, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False)]

		self.levels[2]	=	[(137, 0, 70, 14, 0, 0, False, False),
							(0, 98, 63, 12, 0, 0, False, False),
							(161, 120, 55, 47, 0, 0, False, False),
							(290, 209, 46, 46, 0, 0, False, False),
							(193, 224, 98, 31, 0, 0, False, False),
							(426, 259, 54, 12, 0, 0, False, False),
							(208, 305, 48, 13, 0, 0, False, False),
							(321, 306, 56, 14, 0, 0, False, False),
							(0, 0, 8, 360, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False)]

		self.levels[3]	=	[(137, 89, 40, 79, 0, 0, False, False),
							(137, -4, 15, 93, 0, 0, False, False),
							(-5, 216, 69, 16, 0, 0, False, False),
							(137, 217, 71, 16, 0, 0, False, False),
							(329, 0, 17, 16, 0, 0, False, False),
							(329, 73, 17, 88, 0, 0, False, False),
							(297, 161, 49, 71, 0, 0, False, False),
							(345, 73, 55, 16, 0, 0, False, False),
							(434, 129, 46, 15, 0, 0, False, False),
							(137, 321, 71, 39, 0, 0, False, False),
							(0, 0, 8, 360, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False)]

		self.levels[4]	=	[(40, 88, 31, 15, 0, 0, False, False),
							(160, 57, 32, 14, 0, 0, False, False),
							(225, 72, 31, 15, 0, 0, False, False),
							(152, 0, 176, 14, 0, 0, False, False),
							(288, 88, 31, 15, 0, 0, False, False),
							(441, 161, 39, 14, 0, 0, False, False),
							(0, 241, 39, 14, 0, 0, False, False),
							(329, 241, 38, 14, 0, 0, False, False),
							(112, 313, 40, 15, 0, 0, False, False),
							(137, 327, 15, 33, 0, 0, False, False),
							(328, 312, 40, 16, 0, 0, False, False),
							(328, 328, 16, 32, 0, 0, False, False),
							(0, 0, 8, 360, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False)]

		self.levels[5]	=	[(153, 329, 173, 30, 0, 0, False, False),
							(0, 184, 55, 15, 0, 0, False, False),
							(57, 72, 39, 16, 0, 0, False, False),
							(80, 88, 16, 39, 0, 0, False, False),
							(96, 112, 95, 16, 0, 0, False, False),
							(0, 0, 136, 15, 0, 0, False, False),
							(136, 0, 54, 55, 0, 0, False, False),
							(129, 241, 47, 15, 0, 0, False, False),
							(289, 80, 191, 175, 0, 0, False, False),
							(290, 0, 39, 24, 0, 0, False, False),
							(329, 0, 94, 39, 0, 0, False, False),
							(0, 0, 8, 360, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False)]

		self.levels[6]	=	[(0, 0, 88, 17, 0, 0, False, False),
							(0, 168, 33, 15, 0, 0, False, False),
							(0, 239, 104, 120, 0, 0, True, False),
							(0, 183, 33, 56, 0, 0, False, False),
							(129, 48, 39, 24, 0, 0, False, False),
							(153, 0, 15, 48, 0, 0, False, False),
							(104, 72, 126, 31, 0, 0, False, False),
							(152, 103, 78, 56, 0, 0, False, False),
							(152, 159, 39, 34, 0, 0, False, False),
							(136, 239, 72, 8, 0, 0, False, False),
							(184, 248, 7, 47, 0, 0, False, False),
							(191, 248, 17, 7, 0, 0, False, False),
							(209, 0, 56, 23, 0, 0, False, False),
							(265, 0, 31, 17, 0, 0, False, False),
							(290, 153, 94, 7, 0, 0, False, False),
							(368, 95, 16, 59, 0, 0, True, False),
							(384, 113, 40, 23, 0, 0, False, False),
							(457, 113, 23, 23, 0, 0, False, False),
							(290, 208, 134, 15, 0, 0, False, False),
							(290, 223, 14, 136, 0, 0, False, False),
							(304, 305, 64, 40, 0, 0, False, False),
							(304, 345, 120, 15, 0, 0, False, False),
							(353, 223, 15, 24, 0, 0, False, False),
							(290, 110, 46, 10, 0, 0, True, False),
							(385, 0, 95, 48, 0, 0, False, False),
							(0, 0, 8, 360, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False),
							(33, 168, 71, 71, (-1, 1), 0, False, False),
							(136, 247, 48, 48, (-1, -1), 0, False, False),
							(290, 64, 46, 46, (1, 1), 0, False, False),
							(336, 48, 17, 16, (1, 1), 0, False, False),
							(336, 64, 17, 15, (1, -1), 0, False, False),
							(353, 33, 15, 15, (1, 1), 0, False, False),
							(368, 16, 17, 17, (1, 1), 0, False, False),
							(368, 33, 17, 15, (1, 1), 0, False, False),
							(353, 48, 15, 16, (1, -1), 0, False, False),
							(104, 269, 87, 90, (-1, 1), 0, False, False),
							(265, 17, 31, 29, (1, -1), 0, False, False),
							(368, 80, 16, 15, (1, 1), 0, False, False),
							(104, 48, 25, 24, (1, 1), 0, False, False)]

		self.levels[7]	=	[(0, 144, 248, 40, 0, 0, False, False),
							(0, 184, 72, 72, 0, 0, False, False),
							(0, 256, 24, 104, 0, 0, False, False),
							(0, 64, 32, 80, 0, 0, False, False),
							(24, 344, 64, 15, 0, 0, False, False),
							(223, 24, 24, 63, 0, 0, True, False),
							(88, 0, 135, 87, 0, 0, False, False),
							(152, 328, 16, 32, 0, 0, False, False),
							(249, 353, 47, 7, 0, 0, False, False),
							(208, 344, 41, 15, 0, 0, False, False),
							(434, 0, 46, 87, 0, 0, False, False),
							(434, 225, 46, 135, 0, 0, False, False),
							(384, 320, 50, 40, 0, 0, True, False),
							(153, 241, 94, 31, 0, 0, False, False),
							(153, 272, 94, 7, 0, 0, False, False),
							(240, 279, 7, 25, 0, 0, False, False),
							(247, 287, 16, 18, 0, 0, False, False),
							(0, 0, 8, 360, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False),
							(223, 0, 24, 24, (-1, 1), 0, False, False),
							(249, 344, 9, 9, (-1, 1), 0, False, False),
							(384, 270, 50, 50, (1, 1), 0, False, False),
							(247, 272, 16, 15, (-1, 1), 0, False, False),
							(216, 279, 24, 25, (-1, -1), 0, False, False),
							(262, 287, 18, 17, (-1, 1), 0, False, False),
							(279, 304, 18, 16, (-1, 1), 0, False, False),
							(262, 304, 18, 16, (-1, -1), 0, False, False)]

		self.levels[8]	=	[(0, 0, 102, 17, 0, 0, False, False),
							(154, 0, 70, 17, 0, 0, False, False),
							(208, 17, 16, 143, 0, 0, False, False),
							(0, 167, 31, 24, 0, 0, False, False),
							(176, 136, 32, 24, 0, 0, False, False),
							(88, 89, 16, 119, 0, 0, False, False),
							(88, 208, 47, 152, 0, 0, False, False),
							(65, 296, 23, 24, 0, 0, False, False),
							(224, 96, 31, 64, 0, 0, False, False),
							(393, 97, 30, 31, 0, 0, False, False),
							(393, 0, 87, 17, 0, 0, False, False),
							(199, 207, 33, 66, 0, 0, False, False),
							(296, 207, 31, 66, 0, 0, False, False),
							(391, 207, 33, 66, 0, 0, False, False),
							(0, 0, 8, 360, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False),
							(135, 272, 89, 88, (-1, 1), 0, False, False),
							(431, 312, 49, 48, (1, 1), 0, False, False)]

		self.levels[9]	=	[(0, 185, 56, 175, 0, 0, False, False),
							(56, 328, 48, 32, 0, 0, False, False),
							(154, 233, 68, 127, 0, 0, False, False),
							(393, 329, 87, 31, 0, 0, False, False),
							(152, 104, 47, 32, 0, 0, False, False),
							(199, 120, 281, 16, 0, 0, False, False),
							(152, 0, 47, 47, 0, 0, False, False),
							(248, 89, 48, 31, 0, 0, False, False),
							(344, 97, 49, 23, 0, 0, False, False),
							(248, 0, 48, 48, 0, 0, False, False),
							(344, 0, 49, 49, 0, 0, False, False),
							(440, 88, 40, 32, 0, 0, False, False),
							(0, 0, 8, 360, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False),
							(56, 279, 48, 49, (-1, 1), 0, False, False)]

		self.levels[10]	=	[(120, 0, 33, 9, 0, 0, False, False),
							(153, 0, 47, 40, 0, 0, False, False),
							(153, 40, 23, 40, 0, 0, False, False),
							(153, 80, 47, 24, 0, 0, False, False),
							(153, 168, 47, 32, 0, 0, False, False),
							(8, 120, 24, 25, 0, 0, False, False),
							(8, 209, 32, 15, 0, 0, False, False),
							(153, 240, 47, 120, 0, 0, False, False),
							(248, 0, 47, 8, 0, 0, False, False),
							(248, 48, 47, 15, 0, 0, False, False),
							(248, 113, 47, 63, 0, 0, False, False),
							(273, 63, 22, 50, 0, 0, False, False),
							(249, 240, 46, 32, 0, 0, False, False),
							(249, 320, 46, 40, 0, 0, False, False),
							(344, 0, 48, 63, 0, 0, False, False),
							(344, 128, 48, 32, 0, 0, False, False),
							(344, 224, 48, 32, 0, 0, False, False),
							(344, 344, 48, 15, 0, 0, False, False),
							(441, 48, 39, 15, 0, 0, False, False),
							(440, 128, 40, 34, 0, 0, False, False),
							(0, 0, 8, 360, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False),
							(32, 120, 24, 25, (-1, 1), 0, False, False)]

		self.levels[11]	=	[(0, 217, 24, 14, 0, 0, False, False),
							(121, 345, 79, 15, 0, 0, False, False),
							(152, 185, 48, 160, 0, 0, False, False),
							(248, 312, 48, 47, 0, 0, False, False),
							(344, 344, 48, 16, 0, 0, False, False),
							(424, 232, 56, 32, 0, 0, False, False),
							(296, 128, 32, 32, 0, 0, False, False),
							(152, 81, 48, 55, 0, 0, True, False),
							(200, 33, 22, 48, 0, 0, False, False),
							(222, 0, 74, 7, 0, 0, False, False),
							(222, 7, 48, 26, 0, 0, False, False),
							(416, 0, 64, 15, 0, 0, False, False),
							(0, 0, 8, 360, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False),
							(152, 33, 48, 48, (1, 1), 0, False, False),
							(200, 81, 22, 24, (1, -1), 0, False, False),
							(222, 33, 48, 48, (1, -1), 0, False, False),
							(200, 10, 22, 23, (1, 1), 0, False, False),
							(270, 7, 26, 26, (1, -1), 0, False, False)]

		self.levels[12]	=	[(80, 201, 40, 39, 0, 0, False, False),
							(224, 272, 72, 88, 0, 0, False, False),
							(208, 272, 16, 16, 0, 0, False, False),
							(225, 0, 30, 15, 0, 0, False, False),
							(225, 97, 30, 95, 0, 0, False, False),
							(241, 192, 14, 40, 0, 0, False, False),
							(344, 112, 32, 48, 0, 0, False, False),
							(416, 345, 64, 15, 0, 0, False, False),
							(441, 32, 39, 31, 0, 0, False, False),
							(0, 0, 8, 360, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False)]

		self.levels[13]	=	[(0, 0, 160, 32, 0, 0, False, False),
							(191, 200, 25, 80, 0, 0, False, False),
							(216, 97, 63, 15, 0, 0, False, False),
							(361, 137, 62, 15, 0, 0, False, False),
							(216, 264, 64, 16, 0, 0, False, False),
							(224, 279, 31, 81, 0, 0, False, False),
							(255, 280, 25, 25, 0, 0, False, False),
							(0, 0, 8, 360, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False),
							(255, 305, 25, 21, (1, -1), 0, False, False)]

		self.levels[14]	=	[(0, 0, 8, 360, 0, 0, False, False),
							(8, 80, 48, 153, 0, 0, False, False),
							(56, 111, 32, 122, 0, 0, True, False),
							(8, 305, 87, 55, 0, 0, False, False),
							(95, 328, 65, 32, 0, 0, False, False),
							(191, 80, 42, 55, 0, 0, False, False),
							(169, 88, 22, 47, 0, 0, True, False),
							(233, 88, 23, 47, 0, 0, True, False),
							(337, 224, 135, 16, 0, 0, False, False),
							(385, 240, 87, 16, 0, 0, False, False),
							(385, 196, 87, 28, 0, 0, False, False),
							(409, 168, 63, 28, 0, 0, False, False),
							(408, 79, 64, 8, 0, 0, True, False),
							(472, 15, 8, 345, 0, 0, False, False),
							(88, 225, 72, 8, 0, 0, True, False),
							(408, 15, 64, 64, (1, 1), 0, False, False),
							(8, 0, 23, 23, (1, -1), 0, False, False),
							(56, 80, 32, 31, (-1, 1), 0, False, False),
							(88, 151, 72, 73, (-1, 1), 0, False, False),
							(169, 64, 22, 24, (1, 1), 0, False, False),
							(233, 64, 23, 24, (-1, 1), 0, False, False),
							(381, 168, 28, 28, (1, 1), 0, False, False)]

		self.levels[15]	=	[(0, 0, 8, 360, 0, 0, False, False),
							(8, 107, 71, 69, 0, 0, False, False),
							(8, 27, 40, 5, 0, 0, False, False),
							(8, 80, 48, 27, 0, 0, False, False),
							(8, 312, 55, 16, 0, 0, False, False),
							(8, 328, 23, 32, 0, 0, False, False),
							(224, 272, 56, 16, 0, 0, False, False),
							(256, 288, 24, 40, 0, 0, False, False),
							(184, 152, 72, 16, 0, 0, False, False),
							(232, 96, 80, 16, 0, 0, False, False),
							(256, 112, 24, 120, 0, 0, False, False),
							(8, 0, 16, 27, 0, 0, False, False),
							(328, 272, 24, 56, 0, 0, False, False),
							(400, 288, 24, 40, 0, 0, False, False),
							(392, 176, 32, 32, 0, 0, False, False),
							(400, 0, 32, 16, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False),
							(24, 0, 26, 27, (-1, 1), 0, False, False),
							(56, 80, 26, 27, (-1, 1), 0, False, False)]

		self.levels[16]	=	[(0, 0, 8, 360, 0, 0, False, False),
							(96, 0, 16, 200, 0, 0, False, False),
							(72, 48, 24, 32, 0, 0, False, False),
							(48, 64, 24, 16, 0, 0, False, False),
							(72, 168, 24, 32, 0, 0, False, False),
							(48, 184, 24, 16, 0, 0, False, False),
							(8, 256, 104, 16, 0, 0, False, False),
							(232, 256, 87, 16, 0, 0, False, False),
							(280, 128, 16, 128, 0, 0, True, False),
							(296, 224, 23, 32, 0, 0, False, False),
							(232, 128, 16, 72, 0, 0, False, False),
							(400, 312, 32, 48, 0, 0, False, False),
							(440, 168, 32, 16, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False),
							(8, 344, 16, 16, (-1, 1), 0, False, False),
							(280, 112, 16, 16, (-1, 1), 0, False, False),
							(232, 112, 16, 16, (1, 1), 0, False, False)]

		self.levels[17]	=	[(0, 0, 8, 152, 0, 0, False, False),
							(0, 201, 8, 159, 0, 0, False, False),
							(8, 0, 137, 8, 0, 0, False, False),
							(145, 0, 15, 96, 0, 0, False, False),
							(8, 120, 24, 32, 0, 0, False, False),
							(32, 136, 24, 16, 0, 0, False, False),
							(112, 136, 48, 105, 0, 0, False, False),
							(72, 241, 40, 55, 0, 0, False, False),
							(47, 296, 65, 16, 0, 0, False, False),
							(96, 312, 16, 48, 0, 0, False, False),
							(112, 304, 32, 16, 0, 0, False, False),
							(248, 280, 40, 16, 0, 0, False, False),
							(288, 280, 40, 64, 0, 0, False, False),
							(328, 296, 24, 48, 0, 0, False, False),
							(352, 312, 25, 32, 0, 0, False, False),
							(377, 328, 23, 16, 0, 0, False, False),
							(288, 144, 16, 104, 0, 0, False, False),
							(272, 136, 32, 8, 0, 0, True, False),
							(272, 200, 16, 8, 0, 0, True, False),
							(304, 208, 56, 16, 0, 0, False, False),
							(376, 248, 33, 16, 0, 0, False, False),
							(392, 264, 32, 16, 0, 0, False, False),
							(447, 328, 25, 16, 0, 0, False, False),
							(416, 144, 32, 32, 0, 0, False, False),
							(328, 80, 80, 16, 0, 0, True, False),
							(367, 0, 49, 8, 0, 0, False, False),
							(288, 128, 16, 8, 0, 0, False, False),
							(112, 241, 32, 15, 0, 0, False, False),
							(328, 41, 16, 7, 0, 0, False, False),
							(472, 0, 8, 343, 0, 0, False, False),
							(144, 241, 16, 15, (1, -1), 0, False, False),
							(367, 8, 18, 17, (1, -1), 0, False, False),
							(344, 25, 23, 23, (1, -1), 0, False, False),
							(344, 0, 23, 25, (1, 1), 0, False, False),
							(328, 25, 16, 16, (1, 1), 0, False, False),
							(272, 184, 16, 16, (1, 1), 0, False, False),
							(312, 80, 16, 16, (1, 1), 0, False, False),
							(312, 96, 24, 24, (1, -1), 0, False, False),
							(304, 120, 8, 8, (1, -1), 0, False, False),
							(288, 96, 24, 24, (1, 1), 0, False, False),
							(272, 120, 16, 16, (1, 1), 0, False, False)]

		self.levels[18]	=	[(0, 0, 8, 360, 0, 0, False, False),
							(8, 0, 32, 16, 0, 0, False, False),
							(104, 0, 48, 16, 0, 0, False, False),
							(216, 0, 48, 16, 0, 0, False, False),
							(328, 0, 48, 16, 0, 0, False, False),
							(128, 55, 48, 25, 0, 0, False, False),
							(56, 160, 40, 25, 0, 0, False, False),
							(8, 256, 80, 104, 0, 0, False, False),
							(88, 287, 24, 73, 0, 0, False, False),
							(240, 224, 72, 24, 0, 0, False, False),
							(432, 168, 41, 24, 0, 0, False, False),
							(391, 312, 25, 16, 0, 0, False, False),
							(400, 328, 16, 32, 0, 0, False, False),
							(376, 352, 24, 8, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False),
							(96, 160, 25, 25, (-1, 1), 0, False, False),
							(88, 256, 32, 31, (-1, 1), 0, False, False),
							(112, 311, 49, 48, (-1, 1), 0, False, False),
							(377, 312, 14, 16, (1, 1), 0, False, False),
							(368, 352, 10, 10, (1, 1), 0, False, False)]

		self.levels[19]	=	[(0, 0, 8, 360, 0, 0, False, False),
							(8, 184, 80, 24, 0, 0, False, False),
							(8, 208, 32, 152, 0, 0, False, False),
							(48, 104, 33, 32, 0, 0, False, False),
							(120, 272, 32, 88, 0, 0, False, False),
							(105, 287, 15, 73, 0, 0, False, False),
							(216, 272, 48, 88, 0, 0, False, False),
							(328, 272, 8, 88, 0, 0, False, False),
							(336, 312, 40, 48, 0, 0, True, False),
							(392, 184, 80, 24, 0, 0, False, False),
							(440, 272, 32, 40, 0, 0, False, False),
							(408, 88, 16, 48, 0, 0, False, False),
							(472, 0, 7, 360, 0, 0, False, False),
							(81, 104, 30, 32, (-1, 1), 0, False, False),
							(336, 272, 40, 40, (-1, 1), 0, False, False),
							(105, 272, 15, 15, (1, 1), 0, False, False),
							(363, 88, 45, 48, (1, 1), 0, False, False)]

		self.levels[20]	=	[(0, 0, 8, 360, 0, 0, False, False),
							(8, 0, 8, 287, 0, 0, False, False),
							(16, 0, 152, 40, 0, 0, False, False),
							(80, 232, 48, 56, 0, 0, False, False),
							(128, 232, 16, 16, 0, 0, False, False),
							(216, 288, 24, 48, 0, 0, False, False),
							(240, 312, 40, 24, 0, 0, False, False),
							(288, 184, 16, 16, 0, 0, False, False),
							(304, 184, 23, 32, 0, 0, False, False),
							(289, 0, 39, 16, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False),
							(456, 0, 16, 167, 0, 0, False, False),
							(432, 104, 24, 63, 0, 0, False, False),
							(464, 167, 8, 153, 0, 0, False, False),
							(16, 40, 88, 87, (1, -1), 0, False, False),
							(8, 287, 8, 9, (1, -1), 0, False, False),
							(464, 320, 8, 9, (-1, -1), 0, False, False)]

		self.levels[21]	=	[(8, 0, 56, 112, 0, 0, False, False),
							(0, 0, 8, 360, 0, 0, False, False),
							(8, 232, 40, 56, 0, 0, False, False),
							(8, 336, 159, 23, 0, 0, False, False),
							(128, 192, 8, 96, 0, 0, False, False),
							(48, 256, 80, 31, 0, 0, False, False),
							(136, 280, 31, 8, 0, 0, False, False),
							(256, 320, 72, 16, 0, 0, False, False),
							(288, 336, 40, 24, 0, 0, False, False),
							(272, 240, 72, 40, 0, 0, False, False),
							(344, 264, 81, 16, 0, 0, False, False),
							(425, 224, 24, 56, 0, 0, False, False),
							(449, 0, 31, 280, 0, 0, False, False),
							(456, 280, 24, 80, 0, 0, False, False),
							(304, 104, 8, 88, 0, 0, False, False),
							(48, 232, 24, 24, (-1, 1), 0, False, False),
							(136, 232, 48, 48, (-1, 1), 0, False, False),
							(312, 144, 48, 48, (-1, 1), 0, False, False),
							(104, 232, 24, 24, (1, 1), 0, False, False),
							(256, 144, 48, 48, (1, 1), 0, False, False)]

		self.levels[22]	=	[(0, 0, 8, 360, 0, 0, False, False),
							(8, 104, 24, 256, 0, 0, False, False),
							(32, 224, 32, 136, 0, 0, False, False),
							(144, 200, 40, 8, 0, 0, False, False),
							(128, 320, 40, 8, 0, 0, False, False),
							(319, 168, 41, 8, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False),
							(448, 64, 24, 296, 0, 0, False, False)]

		self.levels[23]	=	[(0, 0, 8, 360, 0, 0, False, False),
							(96, 208, 39, 8, 0, 0, False, False),
							(248, 80, 40, 8, 0, 0, False, False),
							(240, 208, 41, 7, 0, 0, False, False),
							(240, 312, 40, 8, 0, 0, False, False),
							(352, 144, 40, 8, 0, 0, False, False),
							(352, 0, 71, 16, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False)]

		self.levels[24]	=	[(0, 0, 8, 360, 0, 0, False, False),
							(72, 304, 40, 8, 0, 0, False, False),
							(65, 192, 39, 23, 0, 0, False, False),
							(208, 224, 72, 23, 0, 0, False, False),
							(96, 56, 8, 88, 0, 0, False, False),
							(240, 88, 8, 88, 0, 0, False, False),
							(240, 0, 105, 16, 0, 0, False, False),
							(352, 344, 72, 15, 0, 0, False, False),
							(384, 233, 8, 63, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False),
							(104, 96, 48, 48, (-1, 1), 0, False, False),
							(248, 127, 48, 49, (-1, 1), 0, False, False),
							(391, 248, 49, 48, (-1, 1), 0, False, False),
							(48, 96, 48, 48, (1, 1), 0, False, False),
							(192, 127, 48, 49, (1, 1), 0, False, False),
							(336, 248, 48, 48, (1, 1), 0, False, False)]

		self.levels[25]	=	[(0, 0, 8, 360, 0, 0, False, False),
							(8, 118, 24, 147, 0, 0, False, False),
							(32, 216, 24, 49, 0, 0, False, False),
							(152, 0, 40, 144, 0, 0, False, False),
							(192, 93, 56, 51, 0, 0, False, False),
							(152, 191, 136, 49, 0, 0, False, False),
							(293, 296, 51, 63, 0, 0, False, False),
							(208, 312, 85, 18, 0, 0, False, False),
							(240, 331, 53, 29, 0, 0, False, False),
							(231, 0, 153, 16, 0, 0, False, False),
							(440, 94, 32, 57, 0, 0, False, False),
							(448, 191, 24, 26, 0, 0, False, False),
							(472, 0, 8, 359, 0, 0, False, False),
							(8, 265, 48, 46, (1, -1), 0, False, False),
							(208, 331, 32, 29, (-1, -1), 0, False, False),
							(448, 217, 24, 26, (-1, -1), 0, False, False)]

		self.levels[26]	=	[(0, 0, 7, 360, 0, 0, False, False),
							(56, 151, 56, 89, 0, 0, False, True),
							(112, 40, 104, 56, 0, 0, False, True),
							(168, 166, 64, 74, 0, 0, False, True),
							(151, 305, 41, 55, 0, 0, False, True),
							(232, 312, 151, 47, 0, 0, False, True),
							(263, 0, 129, 73, 0, 0, False, False),
							(448, 0, 24, 72, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False)]

		self.levels[27]	=	[(0, 0, 8, 360, 0, 0, False, False),
							(72, 88, 40, 128, 0, 0, False, True),
							(112, 120, 40, 96, 0, 0, False, True),
							(168, 0, 192, 40, 0, 0, False, False),
							(248, 40, 112, 48, 0, 0, False, False),
							(216, 160, 61, 56, 0, 0, False, False),
							(277, 176, 83, 40, 0, 0, False, False),
							(264, 280, 128, 80, 0, 0, False, True),
							(448, 303, 24, 57, 0, 0, False, True),
							(472, 0, 8, 360, 0, 0, False, False)]

		self.levels[28]	=	[(0, 0, 8, 359, 0, 0, False, False),
							(8, 202, 23, 88, 0, 0, False, True),
							(72, 0, 128, 48, 0, 0, False, False),
							(152, 173, 24, 75, 0, 0, False, True),
							(168, 327, 87, 33, 0, 0, False, True),
							(255, 310, 112, 50, 0, 0, False, True),
							(448, 108, 24, 42, 0, 0, False, True),
							(472, 0, 8, 360, 0, 0, False, False),
							(8, 290, 23, 22, (1, -1), 0, False, False),
							(448, 150, 24, 27, (-1, -1), 0, False, False)]

		self.levels[29]	=	[(0, 0, 8, 360, 0, 0, False, False),
							(73, 317, 70, 43, 0, 0, False, True),
							(143, 330, 57, 30, 0, 0, False, True),
							(272, 220, 48, 60, 0, 0, False, True),
							(288, 78, 40, 58, 0, 0, False, True),
							(385, 223, 47, 73, 0, 0, False, True),
							(368, 92, 64, 36, 0, 0, False, False),
							(368, 128, 39, 24, 0, 0, False, False),
							(472, 0, 8, 359, 0, 0, False, False),
							(408, 0, 64, 16, 0, 0, False, False),
							(440, 16, 32, 24, 0, 0, False, False)]

		self.levels[30]	=	[(0, 0, 8, 359, 0, 0, False, False),
							(8, 196, 32, 59, 0, 0, False, True),
							(136, 71, 56, 25, 0, 0, False, True),
							(120, 197, 56, 19, 0, 0, False, True),
							(264, 120, 56, 24, 0, 0, False, True),
							(272, 230, 55, 26, 0, 0, False, True),
							(407, 325, 65, 35, 0, 0, False, True),
							(440, 154, 32, 46, 0, 0, False, True),
							(472, 0, 8, 360, 0, 0, False, False),
							(8, 0, 40, 10, 0, 0, False, False),
							(8, 10, 40, 38, (1, -1), 0, False, False),
							(8, 254, 32, 34, (1, -1), 0, False, False),
							(440, 200, 32, 33, (-1, -1), 0, False, False)]

		self.levels[31]	=	[(0, 0, 8, 360, 0, 0, False, False),
							(8, 0, 8, 113, 0, 0, False, False),
							(16, 0, 24, 49, 0, 0, False, False),
							(16, 94, 184, 19, 0, 0, False, False),
							(72, 0, 24, 49, 0, 0, False, False),
							(96, 0, 289, 16, 0, 0, False, False),
							(385, 0, 23, 49, 0, 0, False, False),
							(279, 95, 193, 18, 0, 0, False, False),
							(440, 0, 32, 49, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False),
							(464, 49, 9, 46, 0, 0, False, False),
							(8, 329, 40, 31, 0, 0, False, False),
							(144, 239, 57, 16, 0, 0, False, False),
							(264, 184, 40, 16, 0, 0, False, False),
							(297, 312, 71, 16, 0, 0, False, False)]

		self.levels[32]	=	[(0, 0, 16, 360, 0, 0, False, False),
							(16, 344, 24, 16, 0, 0, False, False),
							(72, 344, 336, 16, 0, 0, False, False),
							(160, 336, 200, 8, 0, 0, False, False),
							(192, 328, 168, 8, 0, 0, False, False),
							(223, 320, 137, 8, 0, 0, False, False),
							(255, 312, 105, 8, 0, 0, False, False),
							(288, 304, 72, 8, 0, 0, False, False),
							(320, 271, 24, 33, 0, 0, False, False),
							(112, 136, 8, 32, 0, 0, False, False),
							(152, 216, 8, 64, 0, 0, False, False),
							(184, 120, 8, 32, 0, 0, False, False),
							(128, 0, 8, 32, 0, 0, False, False),
							(232, 216, 8, 32, 0, 0, False, False),
							(288, 152, 8, 32, 0, 0, False, False),
							(312, 56, 8, 33, 0, 0, False, False),
							(352, -2, 8, 34, 0, 0, False, False),
							(408, 80, 8, 32, 0, 0, False, False),
							(464, 0, 16, 360, 0, 0, False, False),
							(440, 344, 24, 16, 0, 0, False, False)]

		self.levels[33]	=	[(0, 0, 16, 360, 0, 0, False, False),
							(96, 0, 64, 16, 0, 0, False, False),
							(320, 0, 64, 16, 0, 0, False, False),
							(112, 176, 8, 48, 0, 0, False, False),
							(80, 208, 33, 8, 0, 0, False, False),
							(120, 208, 32, 8, 0, 0, False, False),
							(128, 328, 8, 32, 0, 0, False, False),
							(352, 328, 8, 32, 0, 0, False, False),
							(184, 256, 8, 48, 0, 0, False, False),
							(152, 288, 32, 8, 0, 0, False, False),
							(191, 288, 33, 8, 0, 0, False, False),
							(264, 112, 8, 48, 0, 0, False, False),
							(232, 144, 32, 8, 0, 0, False, False),
							(272, 144, 32, 8, 0, 0, False, False),
							(368, 168, 8, 48, 0, 0, False, False),
							(336, 200, 32, 8, 0, 0, False, False),
							(376, 200, 32, 8, 0, 0, False, False),
							(464, 0, 16, 360, 0, 0, False, False),
							(104, 216, 8, 8, (-1, -1), 0, False, False),
							(176, 296, 8, 8, (-1, -1), 0, False, False),
							(256, 152, 8, 8, (-1, -1), 0, False, False),
							(360, 208, 8, 8, (-1, -1), 0, False, False),
							(120, 216, 8, 8, (1, -1), 0, False, False),
							(192, 296, 8, 8, (1, -1), 0, False, False),
							(272, 152, 8, 8, (1, -1), 0, False, False),
							(376, 208, 8, 8, (1, -1), 0, False, False)]

		self.levels[34]	=	[(0, 0, 8, 360, 0, 0, False, False),
							(8, 265, 16, 7, 0, 0, False, False),
							(8, 272, 8, 88, 0, 0, False, False),
							(112, 0, 16, 200, 0, 0, False, False),
							(96, 168, 16, 32, 0, 0, False, False),
							(96, 248, 32, 112, 0, 0, False, False),
							(128, 248, 8, 7, 0, 0, False, False),
							(127, 344, 33, 16, 0, 0, False, False),
							(352, 248, 32, 112, 0, 0, False, False),
							(320, 344, 32, 16, 0, 0, False, False),
							(304, 0, 64, 16, 0, 0, False, False),
							(352, 16, 16, 184, 0, 0, False, False),
							(368, 177, 16, 23, 0, 0, False, False),
							(344, 248, 8, 8, 0, 0, False, False),
							(184, 72, 8, 48, 0, 0, False, False),
							(152, 104, 32, 8, 0, 0, False, False),
							(192, 104, 32, 8, 0, 0, False, False),
							(288, 136, 8, 48, 0, 0, False, False),
							(256, 168, 32, 8, 0, 0, False, False),
							(296, 168, 32, 8, 0, 0, False, False),
							(456, 264, 16, 8, 0, 0, False, False),
							(472, 0, 8, 359, 0, 0, False, False),
							(465, 272, 8, 87, 0, 0, False, False),
							(96, 152, 16, 16, (1, 1), 0, False, False),
							(456, 248, 16, 16, (1, 1), 0, False, False),
							(8, 249, 16, 16, (-1, 1), 0, False, False),
							(368, 161, 16, 16, (-1, 1), 0, False, False),
							(176, 112, 8, 8, (-1, -1), 0, False, False),
							(280, 176, 8, 8, (-1, -1), 0, False, False),
							(192, 112, 8, 8, (1, -1), 0, False, False),
							(296, 176, 8, 8, (1, -1), 0, False, False)]

		self.levels[35]	=	[(0, 0, 8, 360, 0, 0, False, False),
							(112, 287, 16, 73, 0, 0, True, False),
							(183, 216, 114, 16, 0, 0, False, False),
							(352, 287, 16, 17, 0, 0, True, False),
							(233, 0, 23, 80, 0, 0, False, False),
							(224, 80, 32, 136, 0, 0, False, False),
							(192, 112, 32, 32, 0, 0, False, False),
							(256, 112, 32, 32, 0, 0, False, False),
							(288, 344, 96, 8, 0, 0, False, False),
							(304, 352, 63, 8, 0, 0, False, False),
							(416, 0, 56, 16, 0, 0, False, False),
							(472, -4, 8, 364, 0, 0, False, False),
							(448, 152, 24, 32, 0, 0, False, False),
							(448, 248, 24, 32, 0, 0, False, False),
							(128, 272, 23, 21, (1, -1), 0, False, False),
							(151, 249, 24, 23, (1, -1), 0, False, False),
							(175, 232, 16, 17, (1, -1), 0, False, False),
							(112, 272, 16, 15, (1, 1), 0, False, False),
							(128, 249, 23, 23, (1, 1), 0, False, False),
							(151, 225, 24, 24, (1, 1), 0, False, False),
							(175, 216, 8, 9, (1, 1), 0, False, False),
							(289, 232, 24, 26, (-1, -1), 0, False, False),
							(313, 258, 26, 26, (-1, -1), 0, False, False),
							(339, 284, 13, 11, (-1, -1), 0, False, False),
							(297, 216, 16, 16, (-1, 1), 0, False, False),
							(313, 232, 26, 26, (-1, 1), 0, False, False),
							(339, 258, 13, 14, (-1, 1), 0, False, False),
							(352, 272, 16, 15, (-1, 1), 0, False, False),
							(192, 0, 16, 16, (-1, -1), 0, False, False),
							(208, 0, 16, 16, (1, -1), 0, False, False)]

		self.levels[36]	=	[(0, 0, 8, 360, 0, 1, False, False),
							(48, 0, 32, 16, 0, 1, False, False),
							(152, 0, 32, 17, 0, 1, False, False),
							(8, 200, 41, 64, 0, 1, False, False),
							(120, 272, 48, 25, 0, 1, False, False),
							(127, 297, 33, 16, 0, 1, False, False),
							(144, 95, 48, 26, 0, 1, False, False),
							(152, 121, 33, 39, 0, 1, False, False),
							(264, 104, 48, 24, 0, 1, False, False),
							(272, 129, 32, 39, 0, 1, False, False),
							(440, 0, 40, 152, 0, 1, False, False),
							(472, 152, 8, 208, 0, 1, False, False),
							(416, 328, 56, 32, 0, 1, False, False),
							(264, 264, 48, 24, 0, 1, False, False),
							(264, 288, 40, 16, 0, 1, False, False),
							(232, 304, 24, 56, 0, 1, False, False),
							(197, 352, 35, 8, 0, 1, False, False),
							(49, 200, 57, 57, (-1, 1), 1, False, False),
							(106, 257, 14, 15, (-1, 1), 1, False, False),
							(56, 257, 40, 39, (-1, -1), 1, False, False),
							(96, 272, 24, 24, (-1, -1), 1, False, False),
							(232, 272, 32, 32, (1, 1), 1, False, False),
							(184, 304, 48, 48, (1, 1), 1, False, False),
							(256, 304, 24, 23, (1, -1), 1, False, False),
							(184, 352, 11, 8, (-1, -1), 1, False, False),
							(400, 112, 40, 40, (1, 1), 1, False, False),
							(400, 152, 25, 24, (-1, -1), 1, False, False),
							(425, 152, 24, 24, (1, -1), 1, False, False)]

		self.levels[37]	=	[(0, 0, 8, 219, 0, 1, False, False),
							(88, 0, 128, 16, 0, 1, False, False),
							(256, 0, 136, 16, 0, 1, False, False),
							(40, 288, 49, 25, 0, 1, False, False),
							(48, 313, 32, 47, 0, 1, False, False),
							(144, 288, 48, 24, 0, 1, False, False),
							(152, 312, 32, 48, 0, 1, False, False),
							(176, 144, 48, 24, 0, 1, False, False),
							(263, 264, 49, 24, 0, 1, False, False),
							(280, 64, 48, 24, 0, 1, False, False),
							(392, 88, 48, 25, 0, 1, False, False),
							(457, -2, 15, 34, 0, 1, False, False),
							(432, 320, 40, 24, 0, 1, False, False),
							(440, 344, 32, 16, 0, 1, False, False),
							(456, 224, 16, 16, 0, 1, True, False),
							(472, 0, 8, 360, 0, 1, False, False),
							(215, 288, 27, 24, 0, 1, False, False),
							(192, 238, 50, 50, (1, 1), 1, False, False),
							(242, 192, 46, 46, (1, 1), 1, False, False),
							(260, 238, 31, 26, (1, -1), 1, False, False),
							(291, 216, 21, 22, (1, -1), 1, False, False),
							(288, 192, 24, 24, (-1, 1), 1, False, False),
							(242, 264, 21, 24, (1, -1), 1, False, False),
							(192, 288, 23, 24, (-1, -1), 1, False, False),
							(8, 175, 48, 50, (-1, 1), 1, False, False),
							(30, 225, 26, 23, (1, -1), 1, False, False),
							(6, 225, 24, 23, (-1, -1), 1, False, False),
							(0, 219, 8, 6, (-1, -1), 1, False, False),
							(456, 209, 16, 16, (1, 1), 1, False, False),
							(456, 239, 16, 16, (-1, -1), 1, False, False)]

		self.levels[38]	=	[(0, 0, 8, 360, 0, 1, False, False),
							(112, 0, 32, 16, 0, 1, False, False),
							(88, 184, 24, 176, 0, 1, False, False),
							(112, 272, 104, 88, 0, 1, False, False),
							(112, 241, 72, 31, 0, 1, False, False),
							(263, 288, 24, 72, 0, 1, False, False),
							(256, 295, 7, 65, 0, 1, True, False),
							(287, 328, 88, 32, 0, 1, False, False),
							(375, 344, 17, 16, 0, 1, False, False),
							(248, 96, 120, 24, 0, 1, False, False),
							(448, 0, 24, 16, 0, 1, False, False),
							(472, 0, 8, 360, 0, 1, False, False),
							(456, 240, 16, 120, 0, 1, True, False),
							(112, 184, 56, 57, (-1, 1), 1, False, False),
							(184, 241, 32, 31, (-1, 1), 1, False, False),
							(287, 288, 40, 40, (-1, 1), 1, False, False),
							(375, 328, 17, 16, (-1, 1), 1, False, False),
							(327, 55, 41, 41, (-1, 1), 1, False, False),
							(256, 288, 7, 7, (1, 1), 1, False, False),
							(287, 55, 40, 41, (1, 1), 1, False, False),
							(456, 224, 16, 16, (1, 1), 1, False, False)]

		self.levels[39]	=	[(0, 232, 31, 16, 0, 0, True, False),
							(0, 248, 8, 112, 0, 0, False, False),
							(112, 295, 32, 65, 0, 0, False, False),
							(112, 0, 32, 32, 0, 0, False, False),
							(112, 96, 48, 16, 0, 0, False, False),
							(112, 112, 16, 32, 0, 0, False, False),
							(184, 248, 8, 40, 0, 0, False, False),
							(328, 0, 72, 16, 0, 0, False, False),
							(336, 16, 32, 144, 0, 0, False, False),
							(320, 144, 16, 16, 0, 0, False, False),
							(304, 272, 32, 16, 0, 0, False, False),
							(449, 344, 23, 16, 0, 0, False, False),
							(448, 231, 24, 16, 0, 0, True, False),
							(472, 231, 8, 129, 0, 0, False, False),
							(0, 200, 31, 32, (-1, 1), 1, False, False),
							(448, 200, 32, 31, (1, 1), 1, False, False)]

		self.levels[40]	=	[(88, 0, 48, 16, 0, 0, False, False),
							(113, 16, 23, 40, 0, 0, False, False),
							(104, 128, 40, 16, 0, 0, False, False),
							(113, 144, 31, 216, 0, 0, False, False),
							(248, 120, 32, 16, 0, 0, False, False),
							(216, 248, 32, 16, 0, 0, False, False),
							(336, 0, 32, 96, 0, 0, False, False),
							(328, 168, 39, 16, 0, 0, False, False),
							(352, 96, 16, 72, 0, 0, False, False),
							(336, 184, 32, 24, 0, 0, False, False),
							(328, 344, 72, 16, 0, 0, False, False)]

		self.levels[41]	=	[(113, 0, 55, 16, 0, 0, False, False),
							(113, 16, 31, 24, 0, 0, False, False),
							(89, 344, 47, 16, 0, 0, False, False),
							(160, 160, 33, 16, 0, 0, False, False),
							(336, 0, 32, 16, 0, 0, False, False),
							(336, 96, 32, 72, 0, 0, False, False),
							(336, 240, 32, 120, 0, 0, False, False),
							(232, 296, 33, 16, 0, 0, False, False),
							(231, 176, 8, 40, 0, 0, False, False)]

		self.levels[42]	=	[(48, 184, 16, 16, 0, 0, False, False),
							(48, 328, 16, 16, 0, 0, False, False),
							(112, 344, 56, 16, 0, 0, False, False),
							(112, 144, 256, 120, 0, 0, False, False),
							(336, 264, 32, 96, 0, 0, False, False),
							(368, 144, 63, 7, 0, 0, False, False),
							(425, 128, 6, 16, 0, 0, False, False)]

		for level in self.levels:

			self.levels[level] = list(map(lambda t : (*map(lambda n : n * self.scale, t[0:4]), *t[4:]), self.levels[level])) 

class Platform(pygame.Rect):

	def __init__(self, x, y, width, length, slope = False, slip = False, support = False, snow = False):

		super().__init__(x, y, width, length)

		self.type = "Land"

		if slope:

			self.slope = (slope[0] * length/width, slope[1])

		else:

			self.slope = 0

		if slip:

			self.slip = 0.95
			self.type = "Ice"

		else:
			self.slip = 0.2

		self.support = support

		self.snow = snow

		if snow:

			self.type = "Snow"


class Platforms():

	def __init__(self):

		self.font = pygame.font.Font("flappyfont.ttf", 16)

		self.rectangles = Rectangles()

	def platforms(self, level):

		try:

			return [Platform(*rectangle) for rectangle in self.rectangles.levels[level]]

		except:

			return []

	def blitme(self, screen, level):
#		pass
		for platform in self.platforms(level):

			toptext = self.font.render(str(platform.top), True, (0, 255, 0))
			bottext = self.font.render(str(platform.bottom), True, (0, 255, 0))
			righttext = self.font.render(str(platform.right), True, (0, 255, 0))
			lefttext = self.font.render(str(platform.left), True, (0, 255, 0))
			screen.blit(toptext, (platform.centerx, platform.top))
			screen.blit(bottext, (platform.midbottom))
			screen.blit(righttext, (platform.midright))
			screen.blit(lefttext, (platform.midleft))
			pygame.draw.line(screen, (255, 0, 0), platform.topright, platform.bottomleft, 1)
			pygame.draw.rect(screen, (255, 0, 0), platform, 1)


if __name__ == "__main__":
	pygame.init()
	shit = Platforms()

	for level in range(43):

		platform = shit.platforms(level)

		print(f"self.levels[{level}]\t=\t", end = "")
		print('[', end = "")
		print(*sorted([(rect.x, rect.y, rect.width, rect.height, rect.slope, rect.slip, rect.support, rect.snow) for rect in platform], key = lambda l : type(l[4]) == tuple), sep = ",\n\t\t\t\t\t", end = "")
		print(']\n')