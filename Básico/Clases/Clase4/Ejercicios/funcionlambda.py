#Función normal

def f(x):
	resultado = x**2
	return resultado

print(f(3))

#Lambda: función anónima
#NOTA: Podemos asignarle una variable a la función
g = lambda x: x**2
print(g(5))

#Si no le asinamos una variable a la función entonces 
#sería de esta manera: (poniendo el parámetro después de
#la función)
print((lambda x: x**4)(2))

#Tarea opcional:
#Cómo usar condicionales en una lambda y usarlo con la serie fibonacci
#Se usa el operador ternario