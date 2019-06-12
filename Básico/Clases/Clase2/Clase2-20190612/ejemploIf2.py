#Evaluación de las comparaciones
# == igual que
# =! diferente que
# < menor que 
# > mayor que
# <= menor o igual que
# >= mayor o igual que 

import random #Importamos en modulo random
x=random.randint(1,101) #Usamos la función randint para que nos regrese un número pseudoaleatorio, los parametros que recibe es el rango en el que nos dará el número en este caso entre 1 y 101


if x<50:
	print("El número es menor que 50 y es {0}".format(x))
else:
	print("EL número es mayor que 50 y es {0}".format(x))

####format: Está función remplaza {Número/Índice} por la variable
"""
format puede recibir varios parametros separados por comas
Similar a la una lista todos los parametros se guardan con un índice
Ahora como sólo pasamos un valor y los índices empiezan en 0 
el número ingresado entre los corchetes es 1 y se remplaza por x

"""

