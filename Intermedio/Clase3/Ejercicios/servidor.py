import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = "localhost" #También se puede usar "127.0.0.1"
ip_address = socket.gethostbyname(hostname)#"192.168.3.46" 

print("Servidor {0} ip: {1}".format(hostname, ip_address))

complete_address = (ip_address, 3000) #El segundo parámetro representa al puerto 
#Las ip completas llevan la forma xxx.xxx.xxx.xxx:puerto
sock.bind(complete_address)
#Ejecute el proceso en el puerto 3000
#Enlazar, a que computadora nos vaos a conectr y por que camino nos vamos a conectar(el puerto)

sock.listen(1)
#Siempre escucha lo que entra por ese puerto, por eso tiene un ciclo infinito

while True:
	#Detectar las conexiones
	print("Esperando cliente...")
	conexion, direccion_cliente = sock.accept()

	while True:
		#Conectar con servidor
		try:
			print("Cliente desde: {0}".format(direccion_cliente))
			data = conexion.recv(64)
			#Recibe bytes (recv)
			#data: Objeto de tipo bytes
			#64: Tamaño de los chumps que pasamos, en bytes.
			if data:
				#Recibe bytes y lo imprimos despues de convertirlo a string
				print(data.decode())
				#Contestamos con una cadena y lo convertimos a bytes
				respuesta = input(">> ")
				#Para que sepa que codificación estamos usando, pudo haber sifo ASCII o utf
				# Después lo convertimos a bytes
				respuesta_bytes = respuesta.encode("utf-8")
				# y se lo mandamos al cliente
				conexion.sendall(respuesta_bytes)
		except Exception as e:
			print(e)
			print("no hay clientes disponibles")
			break
		finally:
				conexion.close()

