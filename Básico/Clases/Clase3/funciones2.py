#Asignar valores por defecto a los parámetros
def hola(a=5, b=6):
	print("La suma es ", a+b)

# * desempaque, te regresa el valor 
def argumentos(*galileo):
	for x in galileo:
		print(x)

# * desempaca los dos valores del diccionario: llave y valores 
def diccionarios(**diccio):
	#En for podemos utilizar dos variables 
	#Items te regresa los valores
	for x,y in diccio.items():
		print(x+"  :  "+y)

hola()
hola(2,3)
argumentos(6,"hola",7,"mamamia","python")
diccionarios(nombre="Aldo",edad="21",dinero="mucho",comer="verdura")

numero = 20
print(numero)
def prueba():
	#Variables locales
	global numero
	numero = 15
	print(numero)

prueba()
print(numero)

