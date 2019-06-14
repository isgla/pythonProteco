#Función normal

def f(x):
	resultado = x**2
	return resultado


#Lambda
g = lambda x: x**2
print(f(3))
print(g(5))

print((lambda x: x**4)(2))

#Tarea opcional:
#Cómo usar condicionales en una lambda y usarlo con la serie Fibo