import threading

def imprime(numero):
	print("Hilo: ",numero)

#for i in range(15):
#	hilo = threading.Thread(target = imprime, args = (i,3))
#	hilo.start()

hilo = threading.Thread(target = imprime, args = (1,))
#en args = (1,) la coma significa que puede haber varios parámetros
hilo2 = threading.Thread(target = imprime, args = (2,))
hilo.start()
hilo2.start()