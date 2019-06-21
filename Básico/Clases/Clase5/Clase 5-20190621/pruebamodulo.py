#import modulo
from modulo import areaCirculo
import modulo as mo

while True:
	print("Cálculo de áreas\n")
	print("\t1.- Cuadrado")
	print("\t2.- Triangulo")
	print("\t3.- Circulo")
	print("\t4.- Rectangulo")
	opcion = int(input("Ingresa la opción que deseas: "))
	if opcion == 1:
		lado = int(input("Dame el lado: "))
		resultado = mo.areaCuadrado(lado)
		print(resultado)
	elif opcion == 2:
		base = int(input("Dame la base: "))
		altura = int(input("Dame la altura: "))
		print(mo.areaTriangulo(base,altura))
	elif opcion == 3:
		radio = int(input("Dame el radio: "))
		print(areaCirculo(radio))
	elif opcion == 4:
		base = int(input("Dame la base: "))
		altura = int(input("Dame la altura: "))
		print(mo.areaRectangulo(base,altura))
	else:
		break