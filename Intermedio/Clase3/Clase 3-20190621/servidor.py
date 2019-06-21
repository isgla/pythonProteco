import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = "localhost" # Tambièn se puede unsar "127.0.0.1"
ip_addres = "192.168.3.13"

print("Servidor {0} ip: {1}".format(hostname, ip_addres))

complete_address = (ip_addres, 5000) # El segundo parámetro representa al puerto
# las ip completas llevan la forma xxx.xxx.xxx.xxx:puerto
sock.bind(complete_address)

sock.listen(1)


while True:


	print("Esperando cliente...")
	conexion, direccion_cliente = sock.accept()
	try:
		while True:
			print("Cliente desde: {0}".format(direccion_cliente))
			data = conexion.recv(64)
			if data:
				print(data.decode())
				respuesta = input(">> ")
				respuesta_bytes = respuesta.encode("utf-8")
				conexion.sendall(respuesta_bytes)
	except Exception as e:
		print(e)
		print("no hay clientes disponibles")
		break
	finally:
		conexion.close()

















