
class animal:

	def __init__(self):

		self.x = 1

	def mult(self):

		print('s')

class dog(animal):

	def __init__(self):

		super().__init__()
		self.y = 2

	def mult(self):

		print('s')

class eagle(animal, dog):

	def __init__(self):

		super().__init()
		self.z = 3

h = eagle()

h.mult()
