import threading
import socket

class HiloCliente(threading.Thread):
	def __init__(self, socketCliente):
		threading.Thread.__init__(self)
		self.socketCliente = socketCliente

	def run(self):
		while True:
			mensaje = self.socketCliente.recv(1024).decode()
			if mensaje == "adios":
				break
			print("Mensaje: {0} desde: {1}".format(mensaje,str(threading.current_thread())))

		self.socketCliente.close()

hilos = []

socketServidor = socket.socket()
socketServidor.bind(("192.168.3.13",9000))
print("Esperando conexiones...")
socketServidor.listen(1)

while True:
	try:
		socketServidor.settimeout(1)
		#print("Esperando conexión....")
		socketCliente, direccion = socketServidor.accept()
		print("Conectado desde: ", direccion[0])
	except socket.timeout:
		#print("Esperando...")
		continue

	hilo = HiloCliente(socketCliente)
	hilos.append(hilo)
	hilo.start()
	print(hilos)

socketServidor.close()


