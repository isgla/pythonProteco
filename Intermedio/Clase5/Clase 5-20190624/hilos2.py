import threading

def imprime(numero):
	print("Hilo: ",numero)
	for i in range(15):
		print(i)

#for i in range(15):
#	hilo = threading.Thread(target = imprime, args = (i,))
#	hilo.start()
hilo = threading.Thread(target = imprime, args = (1,))
hilo2 = threading.Thread(target = imprime, args = (2,))
hilo.start()
hilo2.start()