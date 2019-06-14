class Persona:
	planeta = "Tierra"

	def __init__(self, nombre, apellido, edad):
		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad
		self.habilidades = []
		self.__telefono = "55555555"

	def get_telefono(self):
		return self.__telefono

	def set_telefono(self, nuevo_numero):
		self.__telefono = nuevo_numero

aldo = Persona("Aldo", "Vazquez", 21)
print(aldo.get_telefono())
aldo.set_telefono("5534056152")
print(aldo.get_telefono())

'''
El teléfono es privado entonces 
	print(aldo.__telefono)
da el error:

Traceback (most recent call last):
  File "encapsulamiento.py", line 12, in <module>
    print(aldo.__telefono)
AttributeError: 'Persona' object has no attribute '__telefono'
'''
