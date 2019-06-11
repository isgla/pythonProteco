#Evaluar comparaciones
import random

x=random.randint(1,101)

#Impresión con formato
"""
if x<50:
	print("El número es {0} y es menor a 50".format(x))

else:
	print("El número es {0} y es mayor a 50".format(x))
"""

if x<=10:
	print("El número es {0} y es menor o igual a 10".format(x))

elif x>10 and x<=20:
	print("El número es {0} y es mayor a 10 y menor o igual que 20".format(x))

elif x>20 and x<=30:
	print("El número es {0} y es mayor a 20 y menor o igual que 30".format(x))

else:
	print("El número es {0} y es mayor a 30".format(x))
