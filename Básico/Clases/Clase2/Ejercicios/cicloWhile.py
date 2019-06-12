#Ciclos iterativos

#Importando una función de un módulo
from time import sleep 

#while

x=0
while x < 10:
	print("Este código se está ejecutando por {0} vez".format(x))
	x=x+1
	#Para retrasar dos segundos su impresión
	sleep(2)

