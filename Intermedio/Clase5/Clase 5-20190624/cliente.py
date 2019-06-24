import socket

socketCliente = socket.socket()

socketCliente.connect(("192.168.3.13",3000))

while True:
	mensaje = input("Ingresa tu mensaje: ")
	socketCliente.send(mensaje.encode())
	if mensaje == "adios":
		break

socketCliente.close()