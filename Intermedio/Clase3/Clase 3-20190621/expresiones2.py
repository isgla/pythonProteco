import re


#match() busca el patron al inicio de la cadena
#search() busca el patron no importa donde empiece la cadena
#compile() Me permite guardar mi expresion regular en una variable para después usar los otros métodos (match(), search(), findall())

if re.search("-\d{3}$","099-333"):
	print("Hizo match")

if re.search("pytho.","Este es el curso de python de la sala A"):
	print("Encontré una coincidencia :3")

patron = re.compile("a[3-5]+")

print(patron.match("a55"))

print(patron.findall("ba544 a222 a768 a3555 c55"))

