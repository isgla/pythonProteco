import socket

socketCliente = socket.socket()

#Ponemos dos parámetros: la direccion IP y el puerto.
socketCliente.connect(("192.168.3.13",9000))

while True:
	mensaje = input("Ingresa tu mensaje: ")
	#Mandas los mensaje de cadenas como bytes, necesitas codificar
	socketCliente.send(mensaje.encode())
	if mensaje == "adios":
		break

socketCliente.close()
