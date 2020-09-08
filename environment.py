#!/usr/bin/env python
#
#
#
#

import os
import pickle
import pygame

class Environment:

	def __init__(self):

		os.environ["hitboxes"] = ""
		os.environ["screen_width"], os.environ["screen_height"] = str(480), str(360)
		os.environ["window_scale"] = "1"
		os.environ["fps"] = str(60)
		os.environ["bg_color"] = str((0, 0, 0))
		os.environ["mode"] = "normal"
		os.environ["start"] = ""
		os.environ["active"] = ""
		os.environ["gaming"] = ""
		os.environ["pause"] = "1"
		os.environ["volume"] = "1.0"
		os.environ["music"] = "1"
		os.environ["ambience"] = "1"
		os.environ["sfx"] = "1"
		os.environ["time"] = "0"
		os.environ["jumps"] = "0"
		os.environ["falls"] = "0"
		os.environ["session"] = "0"
		os.environ["attempt"] = "1"
		pygame.mixer.set_num_channels(16)

		self._load_settings()
		self._load_stats()

	def _load_settings(self):	

		if "settings.dat" in os.listdir("Saves"):

			with open("Saves\\settings.dat", "rb") as file:

				state = pickle.load(file)

				os.environ["window_scale"] = state["window_scale"]
				os.environ["sfx"] = state["sfx"]
				os.environ["music"] = state["music"]
				os.environ["ambience"] = state["ambience"]
				os.environ["volume"] = state["volume"]

	def _load_stats(self):

		if "save.dat" in os.listdir("Saves"):

			with open("Saves\\save.dat", "rb") as file:

				state = pickle.load(file)

				os.environ["time"] = str(state["KING"]["time"])
				os.environ["jumps"] = str(state["KING"]["jumps"])
				os.environ["falls"] = str(state["KING"]["falls"])

		if "permanent.dat" in os.listdir("Saves"):

			with open("Saves\\permanent.dat", "rb") as file:

				state = pickle.load(file)

				os.environ["session"] = str(state["session"])
				os.environ["attempt"] = str(state["attempt"])

	def save(self):

		settings, permanent = self.game_state()

		with open("Saves\\settings.dat", "wb") as file:

			pickle.dump(settings, file)

		with open("Saves\\permanent.dat", "wb") as file:

			pickle.dump(permanent, file)

	def game_state(self):

		settings_state = {

					"window_scale" : os.environ.get("window_scale"),
					"sfx" : os.environ.get("sfx"),
					"music" : os.environ.get("music"),
					"ambience" : os.environ.get("ambience"),
					"volume" : os.environ.get("volume")
		}

		permanent_state = {

					"session" : os.environ.get("session"),
					"attempt" : os.environ.get("attempt")
		}

		return settings_state, permanent_state