'''
Decoradores
Se trata de una función que recibe como parámetro otra función 
y devuelve una función.
Sirve para agregar más acciones a nuestra función
'''

#Definición de un decorador
def agregar(funcion):
	def decorar():
		print("Está a punto de iniciar mi función.")
		funcion()
		print("Terminó la ejecución")
	return decorar

@agregar
def hola():
	print("Hola")

#Otra notación en lugar de poner @agregar es:
#agregar(hola)()

hola()