#hilos - threads

import threading

#Hilos en python se implementan con la clase Thread

class Hilo(threading.Thread):

	def __init__(self, numero):
		threading.Thread.__init__(self)
		self.numero = numero

	#Dentro de este método van las acciones que queremos que hagan los hilos
	def run(self):
		for i in range(50):
			print(i)

hilo = Hilo(1)
hilo2 = Hilo(2)

#Para que los hilos empiecen su ciclo de vida necesitamos el método start()
hilo.start()
hilo2.start()
