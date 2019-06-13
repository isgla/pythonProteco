#Asignar valores por defecto a los parámetros
"""
def hola(a=5,b=6):
	print("La suma es ",a+b)

#Tupla como argumento
def argumentos(*galileo):
	for x in galileo:
		print(x)

#Diccionario como argumento
def diccionarios(**diccio):
	for x,y in diccio.items():
		print(x+" : "+y)


hola()
hola(2,3)
argumentos(6,"hola",7,"mamamia","python")
diccionarios(nombre="Aldo",edad="21",dinero="mucho",comer="verdura")

"""

#Variables globales
numero = 20
print(numero)
def prueba():
	#Variables locales
	global numero
	numero = 15
	print(numero)

prueba()
print(numero)
