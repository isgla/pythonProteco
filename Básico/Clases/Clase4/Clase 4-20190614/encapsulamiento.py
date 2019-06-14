class Persona:

	planeta = "Tierra"

	def __init__(self, nombre, apellido, edad):

		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad
		self.habilidades = []
		self.__telefono = "5555555555"

	def get_telefono(self):

		return self.__telefono

	def set_telefono(self, nuevo_numero):

		self.__telefono = nuevo_numero

aldo = Persona("Aldo", "Vázquez", 21)
print(aldo.get_telefono())
#aldo.__telefono = "3333333333"
telefono = input("Ingresa tu nuevo número: ")
aldo.set_telefono(telefono)
print(aldo.get_telefono())
