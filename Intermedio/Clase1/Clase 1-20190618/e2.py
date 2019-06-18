#bloque try
try:
	x=10/0
#Se ejecuta el bloque except si se realiza una division entre cero
except ZeroDivisionError:
	print("La division entre cero no es posible")
#el bloque else se ejecuta si no hay error en try
else:
	print(x)
