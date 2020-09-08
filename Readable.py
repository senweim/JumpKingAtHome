#!/usr/bin/env python
#
#
#
#

import pygame
import os
import collections
import re
import inspect

class Readables:

	def __init__(self):

		self.font = pygame.font.Font("Fonts\\ttf_pixolde.ttf", 14)

		self.readable_6 = ((304, 278, 29, 27), """I have had enough. My feet hurt from all the jumping, I have fallen too many times to count... How long has it been by now?

												I should just stay here this time, yes, why try when victory is not certain?

												All this struggle, for what? Never have I even been rewarded with as much as a glimpse!

												I could get comfortable here... Yes, maybe I will try again some other time.

												But then again, could it be the legends are true?""")

		self.readable_10 =  ((175, 57, 23, 23), """Jumpers' Poem

												Jumping and falling, my heart is turned cold

												Down here naught can warm it, no not even gold

												So I rise and attempt once again, fearing not

												My heart resting sure that the babe remains hot""")

		self.readable_15 = ((329, 239, 31, 33), """"Town-Hall Board of Notice"

												This abandoned town, which is clearly abandoned, and which no-one lives in,

												is henceforth irrevocably, eternially, foreverally,

												uncancellably and undeniably claimed, by right of previous owners blatant abandonement,

												as the sole property of Merchant Megildus Dreeg.

												In addition I, Megildus Dreeg, shall rename this new shining centre of commerce, it shall hereby be known as Bargainburg!

												Should any legal inquiries or complaints arise, contact *unintelligible*, thank you for your cooperation!""")

		self.readable_21 = ((0, 308, 35, 35),   """Day 187

												It appears my journey is at its end.

												It seems it was not meant to be me after all.

												For so long I believed...

												But when I reached THAT place, there was nothing I could do...

												Perhaps I can find someplace to stay back in Bogtown. 

												I wonder if they will believe me...""")

		self.readables = collections.defaultdict()

		self._load_readables() 

	def _load_readables(self):

		self.readables[6] = Readable(self.readable_6[0], self.readable_6[1], self.font)

		self.readables[10] = Readable(self.readable_10[0], self.readable_10[1], self.font)

		self.readables[15] = Readable(self.readable_15[0], self.readable_15[1], self.font)

		self.readables[21] = Readable(self.readable_21[0], self.readable_21[1], self.font)

class Readable:

	def __init__(self, rect, quote, font):

		self.interval = 10

		self.pause_interval = 360

		self.pause = 0

		self.blit_counter = 0

		self.rect = pygame.Rect(rect)

		self.quote = quote

		self.font = font

		self.line = iter(inspect.cleandoc(quote))

		self.text = ""

		self.channel = pygame.mixer.Channel(9)

		self.channel_counter = 1

		self.audio = pygame.mixer.Sound("Audio\\Misc\\talking.wav")

	def update(self, king):

		if king.idle_counter >= 200 and self.rect.colliderect(king.rect):

			try:

				if not self.blit_counter % self.interval:

					next_letter = next(self.line)

					if next_letter == "\n":

						self.blit_counter = str(self.blit_counter)

					else:

						self.text += next_letter

						if next_letter != " ":

							self.channel.play(self.audio)

				self.blit_counter += 1

			except TypeError:

				self.pause += 1

				if self.pause > self.pause_interval / 4:

					self.pause = 0
					self.blit_counter = int(self.blit_counter)
					self.text = ""

			except StopIteration:

				self.pause += 1

				if self.pause > self.pause_interval:

					self.reset()

		else:

			self.reset()

	def reset(self):

		self.line = iter(inspect.cleandoc(self.quote))
		self.blit_counter = 0
		self.pause = 0
		self.text = ""

	def blitmetext(self, screen):

		if self.text:

			for index, line in enumerate(map(lambda x: x[0], re.findall(r"(([^ .,!?]+[ .,!?]*){0,4})", self.text)[::-1])):

				text = self.font.render(line, True, (255, 255, 255))

				text_x, text_y = self.rect.x - text.get_width(), self.rect.y - (index + 1) * text.get_height()

				if text_x < 0:

					text_x = self.rect.right				

				screen.blit(text, (text_x, text_y))

if __name__ == "__main__":

	text = 			"""I ha"""

	#text2 = iter(text)
	print(*map(lambda x: x[0], re.findall(r"((\w+[ .,!?]*){0,4})", text)))
	
	a = "" + 1