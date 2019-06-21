class Persona:

	def __init__(self, nombre, apellido, edad):

		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad

	def saludar(self):

		print("{nombre} dice hola!".format(nombre=self.nombre))


class Vegetariano(Persona):

	def comer(self):

		print("Lo siento, no como carne...")


class Vegano(Vegetariano):

	def saludar(self):

		print("Hola, soy {nombre} y soy vegano".format(nombre=self.nombre))


	def comer(self):

		print("Yo no como ningún producto animal, ¿Ya mencioné que soy vegano?")


class CrudiVegano(Vegano):

	def __init__(self, nombre, apellido, edad, fruta_favorita, verdura_favorita):

		super().__init__(nombre, apellido, edad)
		self.fruta_favorita = fruta_favorita
		self.verdura_favorita = verdura_favorita

	def comer(self):

		print("Soy {nombre} y solo como cosas crudas como {fruta} y {verdura}".format(nombre=self.nombre, fruta=self.fruta_favorita, verdura=self.verdura_favorita))

class Fantasma:

	def __init__(self, color):

		self.color = color

class ComeAire(CrudiVegano, Fantasma):
	
	def __init__(self, nombre, apellido, edad, fruta_favorita, verdura_favorita, color):

		super(ComeAire, self).__init__(nombre, apellido, edad, fruta_favorita, verdura_favorita)


aldo = Vegetariano("Aldo", "Vázquez", 21)
rodrigo = Vegano("Rodrigo", "Vivas", 23)
derek = CrudiVegano("Derek", "Cortés", 21, "Mango", "Papa")
comeaire = ComeAire("Aldo", "Vázquez", 21, "Mango", "Calabaza", "Blanco")

print(comeaire.nombre)

