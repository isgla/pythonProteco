import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hostname = "localhost" # Tambièn se puede unsar "127.0.0.1"
# ip_addres = socket.gethostbyname(hostname)
ip_addres = "192.168.3.12"

server = (ip_addres, 5000)

sock.connect(server)
print("Conectando al server: {0}".format(ip_addres))

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












