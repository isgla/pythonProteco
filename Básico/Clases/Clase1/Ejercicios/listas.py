x = [1,2,3,4]
y = ["Uno", "Dos", "Tres"]
listavarios = [5,2.4,"Dos", [1,2, [4, "hola"]]]
numeroDeElementos = len(x)

print(numeroDeElementos)

#Indices
print(x[0])
print(y[1][1])
#Comienzas contando desde 0 y te metes al elemento de la lista
print(listavarios[3][2][1][0])

#Para contar en reversa -1,-2....
print(x[-2])

#Manipulacion de listas
x[0] = 10
print(x)

#Agregando el elemento al final de la lista
y.append("Cuatro")
print(y)

#Agregando el elemento donde queramos
y.insert(0, "Nuevo dato")
print(y)

#Metodos para eliminar
#Eliminar por coincidencia
print(x)
x.remove(10)
print(x)

#Eliminar por indice
print(y)
del y[0]
print(y)






