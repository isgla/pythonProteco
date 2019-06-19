import re

try:
	archivo = open("correos.txt","r")
	contenido = archivo.read()
	print("Los correos electrónicos encontrados son: ")


	expresion = re.compile("[\w\.-_]+@[a-zA-Z0-9.-_]+\.[a-zA-Z0-9]+")
	coincidencias = expresion.findall(contenido)
	print(coincidencias)
	archivo.close()
except FileNotFoundError:
	print("No se encontró un archivo con ese nombre")



'''
.+[a-zA-Z]+\..*[com|mx]
No sirve porque antes de la @ podría haber lo que sea
	#Puedo poner un caracter alfanumérico, puntos, guiones bajos
	#arroba
	#de a - z 1 o mas veces
	#\. :Encontrar un punto pero como punto no como metacaracter
	#
	#com o mx
'''