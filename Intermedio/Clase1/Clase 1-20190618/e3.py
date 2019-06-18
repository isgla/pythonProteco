#bloque try
try:
	print(x)
except NameError:
	print("Algo salio mal")
#Siempre va a ejecutarse
finally:
	print("El 'try except' ya termino")