#Funciones en python
import math

def saludar():
	print("Hola a todo Python AM Sala A")

#Observar lo que pasa con el return
def suma(a,b):
	resultado = a+b
	print("La suma es: ", resultado)
	return resultado

#Regresar dos valores
def formgeneral(a,b,c):
	if a==0:
		print("No se puede división entre 0")
		return None,None
	elif b**2-4*a*c < 0:
		print("No hay raíces complejas")
		return None,None

	else:
		res1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
		res2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
		return res1,res2

saludar()

x = suma(3,8)
print("EStoy fuera de la función y el resultado es: ",x)

r1, r2 = formgeneral(1,2,1)
print("La primera raíz es: ",r1)
print("La segunda raíz es: ",r2)

r1, r2 = formgeneral(1,2,3)
print("La primera raíz es: ",r1)
print("La segunda raíz es: ",r2)

