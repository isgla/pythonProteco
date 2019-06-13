while True:
	print("1.- Sumar 2 números")
	print("2.- Elevar a potencia")
	print("3.- Imprimir pares del 1 al 100")
	print("4.- Salir")
	opcion = int(input("Elige tu opción: "))
	if opcion == 1:
		num1 = int(input("Ingresa el primer número: "))
		num2 = int(input("Ingresa el segundo número: "))
		print("La suma de los números es: ",num1+num2)
	elif opcion == 2:
		num = int(input("Elige un número para elevar: "))
		pot = int(input("Elige la potencia a elevar: "))
		print("El número {0} elevado a la potencia {1} es {2}".format(num,pot,num**pot))
	elif opcion == 3:
		for x in range(1,101):
			if x%2 == 0:
				print(x)
	elif opcion == 4:
		print("Adios!")
		break
	else:
		print("Elige una opción correcta :3")