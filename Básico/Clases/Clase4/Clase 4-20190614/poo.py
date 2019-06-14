class Persona:

	planeta = "Tierra"

	def __init__(self, nombre, apellido, edad):

		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad
		self.habilidades = []

	def saludar(self):

		print("{nombre} dice: Hola!".format(nombre=self.nombre))

	def saludar_a_otra_persona(self, otra_persona):

		print("{nombre} saluda a {otro}".format(nombre=self.nombre, otro=otra_persona.nombre))

	def aprender(self, nueva_habilidad):

		self.habilidades.append(nueva_habilidad)

	@classmethod
	def respirar(self):

		print("Todas las personas respiramos")

aldo = Persona("Aldo", "Vázquez", 21)
#aldo.saludar()
rodrigo = Persona("Rodrigo", "Vivas", 23)
#print(rodrigo.planeta)
#print(aldo.planeta)
#aldo.saludar_a_otra_persona(rodrigo)
#rodrigo.saludar_a_otra_persona(aldo)
aldo.aprender("Dar clases")
rodrigo.aprender("Bailar salsa")
print("Habilidades de Aldo: {habs}".format(habs=aldo.habilidades))

Persona.respirar()

