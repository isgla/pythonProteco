x=0
from time import sleep #importamos la función sleep->duerme la pantalla

while x<=10: #Mientras x sea menor que 10
	print("Esto se esta ejecutando por {0} vez".format(x))
	x=x+1 #Incrementamos el valor de x en uno
	sleep(2) #Llamamos la función sleep y pasamos el parametro de segundos que queremos que pare la ejecución
