#Modelo de una red neuronal

"""
Compuerta AND
Entradas       Salidas
0      0          0
0      1          0
1      0          0
1      1          1
"""
import random
import time

def funcion_activacion(x1,x2,w1,w2,b):
	operacion = (x1*w1 + x2*w2) - b #la ecuacion de la recta

	if operacion >= 0:
		return 1
	else:
		return 0

entradas = [(0,0),(0,1),(1,0),(1,1)]
#Son los puntos que queremos obtener (salidas)
salidas = [0,0,0,1]

w1 = 0.5
w2 = 0.2
b = 0.24
eta = 0.25

#El for es para tratar de encontrar las salidas
i = 0
for x in range(32):
	if i == 4:
		i = 0
		time.sleep(2)
		print()

	x1 = entradas[i][0]
	x2 = entradas[i][1]
	D = salidas[i]
	Y = funcion_activacion(x1,x2,w1,w2,b)

	#Indica el estado actual de las variables
	print("x1 {0} x2 = {1} D = {2} Y = {3} w1 = {4} w2 = {5}".format(x1,x2,D,Y,w1,w2))

	#Cálculo de error
	delta = D - Y
	d1 = eta * delta * x1
	d2 = eta * delta * x2

	w1 += d1
	w2 += d2

	#bias
	b = b - eta * delta 
	i+=1

