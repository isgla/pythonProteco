class Uno(object):
	def __init__(self):

		print("Uno")

class Dos(Uno):
	def __init__(self):

		print("Dos")

class Tres(Uno):
	def __init__(self):

		print("Tres")

class Cuatro(Dos, Tres):

	def __init__(self):
		super(Cuatro, self).__init__()
		print("Cuatro")

c = Cuatro()