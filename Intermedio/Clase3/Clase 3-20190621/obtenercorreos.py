import re

try:
	archivo = open("correos.txt","r")
	contenido = archivo.read()
	print("Los correos electrónicos encontrados son: ")
	expresion = re.compile("[A-Za-z0-9\.-_]+@[A-Za-z0-9\.-_]+\.[A-Za-z0-9]+")
	coincidencias = expresion.findall(contenido)
	print(coincidencias)
	archivo.close()
except FileNotFoundError:
	print("No se encontró archivo con ese nombre")