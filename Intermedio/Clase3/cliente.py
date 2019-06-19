import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hostname = "localhost" #También se puede usar "127.0.0.1"
ip_address = "192.168.3.48" #socket.gethostbyname(hostname)

server = (ip_address, 3000)

sock.connect(server)
print("Conectando al server {0}".format(ip_address))

while True:
	message = input(">> ")
	if message.lower() == "adios":
		break
	else:
		message_bytes = message.encode("utf-8")
		sock.sendall(message_bytes)

		respuesta = sock.recv(64)
		respuesta_cadena = respuesta.decode()

		print(respuesta_cadena)

sock.close()

