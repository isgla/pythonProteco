#Paso por valor
"""
Unicamente se manda una copia de mi variable principal a la función
Esto ocurre con tipos de datos simples
Enteros, flotantes
"""
"""
n = 10
def duplicar(parametro):
	parametro = parametro*2
	print(parametro)

print(n)
duplicar(n)
print(n)
"""
#Paso por referencia
"""
Se manda la variable y sus datos son modificados en la función
"""

lista = [2,3,4]

def duplica(l):
	for x in range(len(lista)):
		l[x] = l[x]*2
		print(l[x])
print(lista)
#Para mandar una copia puede ser con lista[:] o con lista.copy()
duplica(lista.copy())
print(lista)