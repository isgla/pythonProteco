import threading
import socket
#192.168.3.13
class HiloCliente(threading.Thread):
	"""docstring for HiloCliente"""
	def __init__(self, socketCliente):
		threading.Thread.__init__(self)
		self.socketCliente = socketCliente

	def run(self):
	#Procesos independientes y son las acciones que ejecutan los clientes
		while True:
			#Decodifica
			mensaje = self.socketCliente.recv(1024).decode()
			#Si es adios, termina el hilo
			if mensaje == "adios":
				break
			#En caso contrario imprime el mensaje
			print("Mensaje: {0} desde {1}".format(mensaje,str(threading.current_thread())))
		#Cierra el hilo
		self.socketCliente.close()

#Para ir guardando todos los clientes
hilos = []

socketServidor = socket.socket()
#Direccion IP y en que puerto esta
socketServidor.bind(("localhost",3000))
print("Esperando conexiones...")
socketServidor.listen(1)

while True:
	#Esta esperando conexiones
	try:
		socketServidor.settimeout(1)
		print("Esperando conexión...")
		#Si la acepta, guardas el socket y la direccion y accept() devuelve los valores
		socketCliente, direccion = socketServidor.accept()
		#Nos devuelve un objeto de tipo tupla entonces en direccion[0] te devuelve la IP
		print("Conectado desde: ", direccion[0])
	except socket.timeout:
		print("Esperando...")
		continue

	#Una vez que aceptas la conexion conviertes al cliente a un hilo
	hilo = HiloCliente(socketCliente)
	#Lo agregas a la lista
	hilos.append(hilo)
	#Iniciar la ejecución
	hilo.start()
	print(hilos)

socketServidor.close()





		