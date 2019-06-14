'''
Generadores
Se definen igual que las funciones pero en vez de utilizar la
palabra "return" utiliza la palabra "yield"
Generan datos en tiempos de ejecución 
Me devuelven un objeto iterable
'''

def generador():
	yield "hola"
	yield "Adios"
	yield 1
	yield (3,3)

a = generador()

#El método next es parte de los métodos mágicos
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
#print(a.__next__()) ya no hay entonces para la iteración

print("-"*30)
print(generador())
#Genera un objeto iterable, si quisiera imprimir cada elemento
#se haría con un ciclo for 

print("-"*30)
#GENERADOR DE NUMEROS PARES
#n Me ayuda a saber cuantos numeros pares me faltan
#a Me ayuda a saber si el número es par o no

def pares(n):
	a = 0
	while n>0:
		if a%2 == 0:
			yield a
			n = n-1
		a+=1

for num in pares(10):
	print(num)