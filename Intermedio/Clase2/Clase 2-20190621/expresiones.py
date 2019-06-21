#Expresiones regulares

# Secuencia especial de caracteres que ayuda a encontrar otras cadenas o conjuntos de cadenas utilizando una sintáxis mantenida en un patrón.

import re

#Si la cadena coincide (hace match) regresa un objeto de tipo match, y si no, regresa None
#match verifica la coincidencia al INICIO de la cadena
if re.match("hola","hola"):
	print("Hizo match")

if re.match(".ola","tola"):
	print("Hizo match 2")

if re.match("\.ola",".ola"):
	print("Hizo match 3")

if re.match("(pyy|j|c)ython","pyyython"):
	print("Hizo match 4")

if re.match("niñ(o|a)s","niñas"):
	print("Hizo match 5")

"""
[0-9]-> Obtiene un caracter del 0 al 9
[a-z] -> Caracter de la a a la z
[A-Z] -> Caracter de la A a la Z
[0-9a-zA-Z] -> Caracter dentro del rango de letras may. y min. y numéricos

[a-f0-5]

"""

if re.match("cadena\d","cadena1s"):
	print("Hizo match 6")

#Negacion ^

if re.match("python[^0-9a-z]","pythonA"):
	print("Hizo match 7")

"""
Cuantificadores
+ , *, ?, {}

+ -> El caracter que precede existe 1 o más veces
* -> El caracter que precede existe 0 o más veces
? -> El caracter que precede puede existir o no (1 o 0 veces)
{n} -> n = numero de veces exactas que queremos que aparezca el caracter

"""

if re.match("python+","pythonnnnn"):
	print("Hizo match 8")

if re.match("python*","pytho"):
	print("Hizo match 9")

if re.match("py(tho)?n","pyn"):
	print("Hizo match 10")

if re.match("pyth{3,5}on","pythhhhon"):
	print("Hizo match 11")

"""
^ -> Debe ir al principio de la cadena
$ -> Debe ir al final de la cadena
"""

if re.match("^(http|https)","http://google.com"):
	print("Hizo match 12")

if re.match("com$","google.com"):
	print("Hizo match 13")

"""
\d -> Equivale [0-9]
\D -> Equivale [^0-9]
\w -> Equivale [a-zA-Z_]
\W -> Equivale [^a-zA-Z_]

"""
