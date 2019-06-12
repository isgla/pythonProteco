""" Evaluaremos más de una condición en un sólo if usando operadores lógicos """
#OR
#NOT

#Usaremos la operación módulo "%" que nos regresa el residuo de la división entre dos números
x = int(input("Ingrese un número: "))

if x%3!=0: #Impares: 1,3,5,7,9...
	print("El número {0} es par".format(x))
if x%3==0 or x%5==0:	#14,28,42...
	print("El número {0} es impar o divisible entre 7".format(x))
if x%3!=0 and not x%5!=0:	#3,9,15,21...
	print("El número {0} es divisible entre 3 pero no entre 6".format(x))