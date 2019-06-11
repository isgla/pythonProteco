#Comparaciones múltiples con operadores lógicos

#OR: "o"

#NOT: "no"

x = int(input("Ingrese un número: "))

# "%" Función módulo: regresa el residuo de la división entre dos números
if x%2!=0: #1,3,5,7,...
	print("El número {0} es impar".format(x))

if x%3==0 or x%5==0:
	print("El número es {0} divisible entre 3 o entre 5".format(x))

if not x%3==0:
	print("El número es {0} no es divisible entre 3".format(x))

