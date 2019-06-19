'''
Ejercicio
Desarrollar un sistema para un supermercado

-El usuario agregará productos al carrito (nombre, cantidad)
Hasta que escriba "salir"
-El supermercado obtendra los precios e imprimirá el ticket para el
usuario en formato txt.
'''

class Producto():
	"""docstring for ClassName"""
	def __init__(self, nombre, precio):
		self.nombre = nombre
		self.precio = precio

	def __str__(self):
		return self.nombre + ": " + str(self.precio)
		

flag = True

lista = []
while flag :
	opc = input(("Escribe salir o escribe sí para agregar productos: "))
	if opc == "salir":
		#Imprimir el ticket
		#Writer es el método que primero convierte en lista y 
		#te permite ir agregando rows, append a la lista. 
		ticket = open("ticket.txt","w")
		for prod in lista:
			ticket.write(str(prod) + "\n")
		ticket.close()
		flag = False
	else:
		x = input("Agrega el producto: ")
		y = int(input("Agrega el precio: "))
		nuevo_producto = Producto(x,y)
		lista.append(nuevo_producto)

	
