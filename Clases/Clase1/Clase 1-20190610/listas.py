#Cadenas
#Una linea
x = 'Hola mundo'
#Cadenas de varias líneas
x = ''' Cadena de varias lineas
asasasa
asdasdas.       asdsada.    asdasdasd. 
'''
#print(x)
#Concatenación de cadenas
x = 'Hola'
y = ' mundo'
z = x + y
#print(z)
#Multiplicación con cadenas
w = x*10
#print(w)
#Método split
y = "Hola-Mundo-Otra-palabra"
x = y.split('a')
#print(x)
#Método join
x = "-".join(["Junta", "las", "palabras"])
#print(x)
#Método find
a = "ferrocarril"
posicion = a.find("rr")
#print(posicion)
#Formatos de impresión de cadenas

numero = 3
numero2 = 5
resultado = numero + numero2
#print("El primer número es: ",numero,"El segundo número es:",numero2,"El resultado es:",resultado)
#Otra manera
#print("El numero: %f"%(numero))
#Método format
#print("El curso de {pythonam} es mejor que el de {pythonpm}".format(pythonam="Rodrigo", pythonpm="Héctor"))
#Lectura de valores por teaclado
#Lo que recibe input lo hace en forma de cadena-string
a = input("Ingresa algo:")
#print("Hola ", a)


x = [1,2,3,4]
y = ["Uno", "Dos", "Tres"]
listavarios = [5, 2.4, "Dos", [1,2,[4, "hola"]]]
numeroDeElementos = len(x)

print(numeroDeElementos)

#Indices
print(x[0])
print(y[1][1])
print(listavarios[3][2][1][0])
print(x[-2])
#Manipulación de listas
x[0] = 10
print(x)
#Agregando elemento al final de la lista
y.append("Cuatro")
print(y)
#Agregando elemento donde queramos
y.insert(0, "Nuevo dato")
print(y)
#Métodos para eliminar
#Eliminar por coincidencia
x.remove(10)
print(x)

#Eliminar por índice
del y[0]
print(y)

































