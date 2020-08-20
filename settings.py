#!/usr/bin/env python
#
#
#
#

import os
import pygame

class Settings:

	def __init__(self):

		os.environ["resolution"] = "2"
		os.environ["screen_width"], os.environ["screen_height"] = str(480 * int(os.environ.get("resolution"))), str(360 * int(os.environ.get("resolution")))
		os.environ["fps"] = str(60)
		os.environ["bg_color"] = str((200, 200, 200))
		os.environ["mode"] = "normal"
		pygame.mixer.set_num_channels(17)
