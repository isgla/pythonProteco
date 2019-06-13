#Funciones en python
import math

def saludar():
	print("Hola a todo Python AM Sala A :3 (Los mejores)")

def suma(a,b):
	resultado = a+b
	print("La suma es: ",resultado)
	return resultado

def chicharronera(a,b,c):
	if a == 0:
		print("No se puede división entre cero :(")
		return None,None
	elif b**2-4*a*c < 0:
		print("Hay raíces complejas")
		return None,None
	else:
		res1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
		res2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
		return res1,res2

saludar()
x = suma(3,8)
r1, r2 = chicharronera(5,2,3)
#print("Estoy fuera de la función y el resultado es ",x)
print("La primer raíz es: ",r1)
print("La segunda raíz es: ",r2)
