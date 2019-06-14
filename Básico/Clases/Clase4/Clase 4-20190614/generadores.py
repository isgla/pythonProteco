"""
Generadores
Se definen igual que las funciones pero en vez de utilizar la palabra "return" utiliza la para "yield"
Generan datos en tiempo de ejecución.
"""

def generador():
	yield "hola"
	yield "Adios"
	yield 1
	yield (3,3)

a = generador()

print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
#print(a.__next__())

#Generador de números pares
#n - Me ayuda a saber cuántos números pares me faltan
#a - Me ayuda a saber si el número es par o no
def pares(n):
	a = 0
	while n>0:
		if a%2 == 0:
			yield a
			n = n-1
		a+=1

for num in pares(10):
	print(num)







