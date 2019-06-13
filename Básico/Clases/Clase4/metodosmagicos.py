class Persona:
	planeta = "Tierra"

	def __init__(self, nombre, apellido, edad):
		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad
		self.habilidades = []

	#Sobreescribimos def __str__(self):
	def __str__(self):
		return self.nombre + " " + self.apellido + " " + str(self.edad)

	def __add__(self, otra_persona):
		return self.edad + otra_persona.edad

aldo = Persona("Aldo", "Vázquez",21)
print(aldo)
'''Imprime la dirección de memoria <__main__.Persona object at 0x10ca72da0>
Porque cada objeto ya tiene un método predeterminado __str__(self), 
así que sobreescribimos'''

rodrigo = Persona("Rodrigo", "Vivas", 23)
print(aldo + rodrigo)
print(len(aldo))