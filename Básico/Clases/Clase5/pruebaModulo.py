import modulo as mo

from modulo import areaCirculo

while True:
	print("Cálculo de áreas\n")#salto de línea
	print("\t1. - Cuadrado")#tabulado
	print("\t2. - Triángulo")
	print("\t3. - Círculo")
	print("\t4. - Rectángulo")
	print("\t5. - Salir")


	opc = int(input("Ingresa la opción que deseas: "))

	if opc == 1:
		lado = int(input("Dame el lado: "))
		resultado = mo.areaCuadrado(lado)
		print(resultado)
	elif opc == 2:
		base = int(input("Dame la base: "))
		altura = int(input("Dame la altura: "))
		print(mo.areaTriangulo(base, altura))
	elif opc == 3:
		radio = int(input("Dame el radio: "))
		print(areaCirculo(radio))
	elif opc == 4:
		base = int(input("Dame la base: "))
		altura = int(input("Dame la altura: "))
		print(mo.areaRectangulo(base, altura))
	else:
		break