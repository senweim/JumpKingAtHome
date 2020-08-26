#!/usr/bin/env python
#
#
#
#

class Rectangle:

	""" SOME AUTISM SHIT LOL """

	def __init__(self, width, length):

		self.length = length

		self.width = width

		self.area = self.length * self.width

		self.perimeter = self.length * 2 + self.width * 2

	def write(self):

		print(f"The are of the rectangle is {self.area}")
		print(f"The perimeter of the rectangle {self.perimter}")

if __name__ == "__main__":

	width = input("What is the width of the rectangle?:		")

	length = input("What is the length of the rectangle?:		")

	rect = Rectangle(width, length)

	rect.write()

