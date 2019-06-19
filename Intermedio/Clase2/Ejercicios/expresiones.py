#Expresiones regulares

# Secuencia especial de caracteres que ayuda aencontrar otras cadenas o 
# conjuntos de cadenas utilizando una sintáxis mantenida en un patrón.

import re #Regular expressions

#Si la cedna coincide (hace match) regresa un objeto de tipo match,
# sino, regresa None
# match verifica la coincidencia al INICIO de la cadena
if re.match("hola", "hola"):
	print("Hizo match")
#expresión regular (secuencia de caracteres), cadena a comparar


#El punto es el comodín
if re.match(".ola", "tola"):
	print("Hizo match 2")

if re.match("....", "topo"):
	print("Hizo match 3")

# Indica que el caracter tome lo tome como es, no como punto. 
# Se le llama caracter de escape
if re.match("\.ola", "hola"):
	print("Hizo match 4")

#Poner varias opciones
if re.match("(pyy|j|c)ython","pyyython"):
	print("Hizo match 5")

if re.match("niñ(o|a)s", "niñas"):
	print("Hizo match 6")

'''
Código alfanumérico
[0-9] -> Obtiene un caracter del 0 al 9
[a-z] -> Caracter de la a a la z
[A-Z] -> Caracter de la A a la Z
[0-9a-zA-Z] -> Caracter dentro del rango del rango de letra may. y min. 
y numéricos

[a-f0-5] Caracter de la a a la f o caracter del 0 al 5
'''

if re.match("cadena[0-9]", "cadena0"):
	print("Hizo match 7")

if re.match("cadena[0-9]", "cadenas"):
	print("Hizo match 8")

if re.match("cadena[0-9]", "cadena1s"):
	print("Hizo match 9")

#Negacion ^
#Después de "python" yo quiero un caracter diferente a lo que le estoy poniendo ahí
if re.match("python[^0-9a-z]","pythonA"):
	print("Hizo match 10")



'''
Cuantificadores
+, *, ?, {}

+ -> El caracter que precede existe 1 o más veces
* -> El caracter que precede existe 0 o más veces
? -> El caracter que precede puede existir o no (1 o 0 veces)
{n} -> n = numero de veces exactas que queremos que aparezca el caracter
'''

# + Coincide con una o más 
if re.match("python+","pythonnnnn"):
	print("Hizo match 11")

if re.match("python*", "pytho"):
	print("Hizo match 12")

if re.match("py(tho)?n","pythothon"):
	print("Hizo match 13")

#5 veces
if re.match("pyth{3,5}on","pythhhhhon"):
	print("Hizo match 14")

'''
^-> Debe de ir al principio de la cadena
$ -> Debe ir al final de la cadena
'''

if re.match("^(http|https)","http://google.com"):
	print("Hizo match 15")

#Debe de terminar con com
if re.match("com$", "google.com"):
	print("Hizo match 16")

if re.match("cadena[0-9]", "cadena1s"):
	print("Hizo match 9")

'''
\d -> Equivale [0-9]
\D -> Equivale [^0-9]
\w -> Equivale [a-zA-Z_] incluir el caracter _ también
\W -> Equivale [^a-zA-Z_] lo mismo pero negado, o sea del 0-9
'''

#Crear una expresión regular para verificar correos






