class Persona:

	def __init__(self, nombre, apellido, edad):
		self.nombre = nombre
		#Hace referencia al parámetro y lo renombras
		self.apellido = apellido
		self.edad = edad

	def saludar(self):
		print("{nombre} dice hola".format(nombre = self.nombre))

class Vegetariano(Persona):

	def comer(self):
		print("{nombre} no come carne".format(nombre = self.nombre))

class Vegano(Vegetariano):
	def saludar(self):
		print("Hola, soy {nombre} y soy vegano".format(nombre=self.nombre))

	def comer(self):
		print("Yo no como ningún producto animal, soy vegano")


class CrudiVegano(Vegano):
	#Sobreescritura del constructor
	def __init__(self, nombre, apellido, edad, fruta_favorita, verdura_favorita):
		super().__init__(nombre, apellido, edad)
		self.fruta_favorita = fruta_favorita
		self.verdura_favorita = verdura_favorita

	def comer(self):
		print("Soy {nombre} y solo como cosas crudas como {fruta} y {verdura}".format(
			nombre = self.nombre, fruta = self.fruta_favorita, verdura = self.verdura_favorita))


class Fantasma:
	def __init__(self, color):
		self.color = color


class ComeAire(CrudiVegano, Fantasma):
	def __init__(self, nombre, apellido, edad, fruta_favorita, verdura_favorita, color):
		super(CrudiVegano, self).__init__(nombre, apellido, edad, fruta_favorita, verdura_favorita)
		super(Fantasma, self).__init__(color)

aldo = Vegetariano("Aldo", "Vázquez", 21)
rodrigo = Vegano("Rodrigo","Vivas", 23)
derek = CrudiVegano("Derek","Cortés", 21, "Mango", "Papas")
comedoraire = ComeAire("Aldo","Vazquez",21, "Mango", "Calabaza", "azul")


aldo.saludar()
aldo.comer()

rodrigo.saludar()
rodrigo.comer()

derek.saludar()
derek.comer()

print(comedoraire.nombre)
print(comedoraire.edad)