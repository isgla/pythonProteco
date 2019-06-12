#Ejercicio (menu de opciones)

menu = """
 MENU DE OPCIONES
 a Sumar dos números
 b Elevar un número a la potencia 
 c Imprime los números pares del 1 al 100
 d Salir\n"""


bandera = True

while bandera:

	print(menu)
	opc = input("Ingresa la letra de la opción que quieras realizar : ")

	if (opc == "a"):
		x = int(input("Ingresa el primer número : "))
		y = int(input("Ingresa el segundo número : "))
		print("La suma es es: ", x + y)
		continue

	elif (opc == "b"):
		x = int(input("Ingresa el número : "))
		y = int(input("Ingresa la potencia : "))
		print("El resultado es: {0} ".format(x**y))
		continue

	elif (opc == "c"):
		print([x for x in range(0,101,2)])

	elif (opc == "d"):
		bandera = False
		break

	else:
		print("\nIngresa una opción válida")
		pass
