#Listas por comprensión

#Más elegantes y más rápido

#Primero va lo que se hace y despues se hara el for

#Primero va lo que se hace y despues se hara el for
alumnos = ['Iker', 'Andres', 'Leonardo']
[x for x in alumnos]


numeros = [1,2,3]
[x**2 for x in numeros]
print(numeros)
print([x**2 for x in numeros])
#Se pone la función antes del for

"""
En lugar de:
numeros = [1,2,3]
cuadrados = []
for numero in numeros:ç
	cuadrados.append(numero**2)
"""


