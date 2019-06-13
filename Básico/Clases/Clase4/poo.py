class Persona:

#init es el método que construye nuestro objeto
#Es el método constructor, y siempre se llama init
#Self es la referencia del objeto
	
	#Atributo de la clase: Será el mismo para todos los objetos de la clase
	#Para acceder a atributos: instancia.atributo
	planeta = "Tierra"

	def __init__(self, nombre, apellido, edad):
		self.nombre = nombre
		#La característica del objeto = nombre que le pasamos como parámetro
		self.apellido = apellido
		self.edad = edad
		#No es necesario que venga como parámetro pero de todas formas todos los 
		#objetos tendrán una lista
		self.habilidades = []

	def saludar(self):
		print("{nombre} dice: ¡Hola!".format(nombre=self.nombre))
		#Nos referimos al campo nombre de self

	def saludar_a_otra_persona(self, otra_persona):
		print("{nombre} saluda a {otro}".format(nombre=self.nombre,
			otro=otra_persona.nombre))

	def aprender(self, nueva_habilidad):
		self.habilidades.append(nueva_habilidad)

	#Vamos a hacer un decorador que es equivalente a un método estático 
	@classmethod
	#Aquí el self toma el valor de la clase
	def respirar(self):
		print("Todas las personas respiramos")




#Instancia de la clase Persona
aldo = Persona("Aldo","Vázquez",21)
aldo.saludar()
rodrigo = Persona("Rodrigo", "Guzmán", 23)

print(rodrigo.planeta)
print(aldo.planeta)

aldo.saludar_a_otra_persona(rodrigo)
#El valor de self lo ocupa aldo, y el valor de rodrigo lo ocupa otra_persona

rodrigo.saludar_a_otra_persona(aldo)


aldo.aprender("Dar clases")
aldo.aprender("Bailar")
print("Habilidades de Aldo: {habs}".format(habs=aldo.habilidades))

Persona.respirar()



''' 
Si pusiera saludar() sin aldo.saludar()

Traceback (most recent call last):
  File "poo.py", line 13, in <module>
    saludar()
NameError: name 'saludar' is not defined
'''
