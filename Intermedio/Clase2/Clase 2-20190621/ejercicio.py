class SuperMercado:

	def __init__(self):

		self.productos = {
			"leche": 20,
			"huevo": 32,
			"harina": 16,
			"mantequilla": 10,
			"azucar": 18
		}


class Producto:

	def __init__(self, nombre, cantidad):

		self.supermercado = SuperMercado()
		self.nombre = nombre
		self.cantidad = cantidad
		self.__precio = self.supermercado.productos[self.nombre]
		self.total = self.get_precio() * self.cantidad


	def get_precio(self):
		return self.__precio


class Carrito:

	def __init__(self, productos):

		self.productos = productos
		self.ticket = open("ticket.txt", "w")


	def calcular_total(self):

		precios = [producto.total for producto in self.productos]
		return sum(precios)

	def generar_ticket(self):

		for producto in productos:
			self.ticket.write("\n"+producto.nombre+"\t\t\t"+str(producto.total))

		self.ticket.write("\n")
		self.ticket.write("-"*50)
		self.ticket.write("\n Total: \t\t\t " + str(self.calcular_total()))


leche = Producto("leche", 10)
huevo = Producto("huevo", 12)
productos = [leche, huevo]
carrito = Carrito(productos)
carrito.generar_ticket()




