import threading

class Hilo(threading.Thread):
	def __init__(self,numero):
		threading.Thread.__init__(self)
		self.numero = numero


	def run(self):
		for i in range(50):
			print(i)


hilo = Hilo(1)
hilo2 = Hilo(2)

hilo.start()
hilo2.start()
	