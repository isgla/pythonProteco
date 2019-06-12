#Declaramos la lista

alumnas = ['Hannah', 'Ariana', 'Malaika']
alumnos = ['Iker', 'Andres', 'Leonardo']


#ciclo for en iterables
for x in alumnas:
	print(x)

print('-'*30)
#For anidados
for x in alumnas:
	print(x)
	for y in alumnos:
		print(x,y)

print('-'*30)
#ciclo for con la función range
for x in range(1,10):
	print(x)
	#imprime del [1,10), i.e., del 1 al 9 
	#porque hace un iterable de ese tamaño 

print('-'*30)
#poner condiciones
for x in range(1,10,2):
	print(x)
	#imprime 1,3,5,7,9, i.e., cada dos elementos



