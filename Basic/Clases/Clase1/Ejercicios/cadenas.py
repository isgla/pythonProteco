#Lista de enteros en python

#Una linea
x = 'Hola mundo'

#Cadenas de varias lineas
x = ''' Cadena de varias lineas
ejemplo1 
ejemplo2
'''

print(x)
#Se sobreescriben

#Concatenación de cadenas
x = 'Hola'
y = ' mundo'
z = x + y
print(z)

#Multiplicación de cadenas
w = x*10
print(w)

#Método split
y = "Hola-Mundo-Otra-palabra"
x = y.split('a')
print(x)

#Método join
x = "-".join(["Junta", "las", "palabras"])
print(x)

#Método find
a = "ferrocarril"
posicion = a.find("rr")
print(posicion)

#Formatos de impresion de cadenas
numero1 = 3
numero2 = 5
resultado = numero1 + numero2
print("El primer número es: ", numero1, "El segundo numero es: ",
	numero2, "El resultado es: ", resultado)

#Otra manera
print("El numero: %f"%(numero1))

#Metodo format
print("El curso de {pythonam} es mejor que el de {pythonpm}".
	format(pythonam="Rodrigo", pythonpm="Hector"))


#Lectura de valores por teclado
#Lo que recibe input lo hace en forma cadena-string
a=input("Ingresa tu nombre:")
print("Hola", a)



