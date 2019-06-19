import re


#match() busca el patrón al inicio de la cadena
#search() busca el patrón,  no importa donde empiece la cadena
#El guión me indica que quiero encontrar una coincidencia con el guión, en cualquier parte de mi cadena
#\d equivale a nums del 0 al 9
#{3} los números se REPITEN 3 veces
if re.search("-\d{3}$","099-333"):
	print("Hizo match")

if re.search("pytho.", "Este es el curso de python de la sala A"):
	print("Encontré una coincidencia")

patron = re.compile("a[3-5]+")

print(patron.match("a55"))

print(patron.findall("ba544 a222 a768 a3555 c55"))

#Debe de haber una a, depués un caracter que esté entre 3 y 5, 
#y el + significa que ese caracter, de 3-5 puede existir m´s de una vez

#Lo puedes guardar en una variable

#Si ya pusiste compile, ya no necesitas poner los dos parámetros en match
#Match si encuentra coincidencia te regresa un objeto match, sino regresa None

	