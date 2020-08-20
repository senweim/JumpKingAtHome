#!/usr/bin/env python
#
#
#
#

import pygame

import sys

class Constructor():

	def __init__(self):

		pygame.init()

		self.screen = pygame.display.set_mode((960, 720))

		self.rect = pygame.Rect(0, 0, 32, 32) 

		self.clock = pygame.time.Clock()

		self.fps = 30

		self.map = pygame.image.load(".\\MG\\27.png")

		self.map = pygame.transform.scale(self.map, (self.map.get_width() * 2, self.map.get_height() * 2))

		self.candle = pygame.image.load("props\\Candle.png")

		self.wack = pygame.Surface((16, 16), pygame.SRCALPHA)

		self.wack.blit(self.candle, (0, 0), (0, 0, 14, 16))

		self.wack = pygame.transform.scale(self.wack, (self.wack.get_width() * 2, self.wack.get_height() * 2))

		self.rectangles = []

		self.pressed = False


		self.font = pygame.font.Font("flappyfont.ttf", 10)

	def check_events(self):

		for event in pygame.event.get():

			if event.type == pygame.QUIT:

				sys.exit()

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_SPACE:

					self.rectangles.append((self.rect.x, self.rect.y, self.rect.w, self.rect.h))

					self.rect = pygame.Rect(0, 0, 32, 32)

				if event.key == pygame.K_d:

					self.rectangles.pop()			

		keys = pygame.key.get_pressed()

		if keys[pygame.K_RIGHT]:

			if self.rect.x < self.screen.get_width():
				self.rect.x += 2

		if keys[pygame.K_LEFT]:

			if self.rect.x > 0:
				self.rect.x -= 2

		if keys[pygame.K_UP]:

			if self.rect.y > 0:

				self.rect.y -= 2

		if keys[pygame.K_DOWN]:

			if self.rect.y < self.screen.get_height():

				self.rect.y += 2

		if keys[pygame.K_l]:

			if self.rect.x < self.screen.get_width():
				self.rect.x += 10

		if keys[pygame.K_j]:

			if self.rect.x > 0:
				self.rect.x -= 10

		if keys[pygame.K_i]:

			if self.rect.y > 0:

				self.rect.y -= 10

		if keys[pygame.K_k]:

			if self.rect.y < self.screen.get_height():

				self.rect.y += 10

		if keys[pygame.K_w]:

			self.rect.inflate_ip(0, 1)

		if keys[pygame.K_q]:

			self.rect.inflate_ip(1, 0)

		if keys[pygame.K_s]:

			self.rect.inflate_ip(0, -1)

		if keys[pygame.K_a]:

			self.rect.inflate_ip(-1, 0)

	def update_screen(self):

		self.screen.fill((200, 200, 200))

		self.screen.blit(self.map, (0, 0))

		# toptext = self.font.render(str(self.rect.top), True, (0, 255, 0))
		# bottext = self.font.render(str(self.rect.bottom), True, (0, 255, 0))
		# righttext = self.font.render(str(self.rect.right), True, (0, 255, 0))
		# lefttext = self.font.render(str(self.rect.left), True, (0, 255, 0))
		# self.screen.blit(toptext, (self.rect.midtop))
		# self.screen.blit(bottext, (self.rect.midbottom))
		# self.screen.blit(righttext, (self.rect.midright))
		# self.screen.blit(lefttext, (self.rect.midleft))

		pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 1)

		#self.screen.blit(self.wack, self.rect)

		for rectangle in self.rectangles:

			#self.screen.blit(self.wack, rectangle)
			pygame.draw.rect(self.screen, (255, 0, 0), rectangle, 1)
			# platform = pygame.Rect(rectangle)
			# toptext = self.font.render(str(platform.top), True, (0, 255, 0))
			# bottext = self.font.render(str(platform.bottom), True, (0, 255, 0))
			# righttext = self.font.render(str(platform.right), True, (0, 255, 0))
			# lefttext = self.font.render(str(platform.left), True, (0, 255, 0))
			# self.screen.blit(toptext, (platform.midtop))
			# self.screen.blit(bottext, (platform.midbottom))
			# self.screen.blit(righttext, (platform.midright))
			# self.screen.blit(lefttext, (platform.midleft))

	def mainloop(self):

		while True:

			self.clock.tick(self.fps)

			self.check_events()

			self.update_screen()

			print(*list(map(lambda l: (l[0]//2, l[1]//2, l[2]//2, l[3]//2, 0, 0), self.rectangles)), sep = ",\n")

			pygame.display.flip()

if __name__ == "__main__":

	game = Constructor()

	game.mainloop()


