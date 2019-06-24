#Tarea 1
#Hannah Isabel González Aburto

#1. Función que indica que el primer número es múltiplo del segundo
def multiplos(x,y):
    if x%y == 0:
        print("El primer número es múltiplo del segundo")
    else:
        print("El primer número no es múltiplo del segundo")


#1
print("¿El primer número es múltiplo del segundo?")
x = int(input("Ingrese el primer número: "))
y = int(input("Ingrese el segundo número: "))
multiplos(x,y)
print("-"*50)

#2
'''
Se tiene una lista de números ordenados de forma creciente en el que 
todos los números (excepto uno) aparecen duplicados. 
Realiza un programa que encuentre el número que no está duplicado dentro 
de la lista.
'''


def numNoMult(listaNumDobles):
    i = 0
    flag = True
    while flag:
        for n in listaNumDobles:
            if i < len(listaNumDobles):
                if n == listaNumDobles[listaNumDobles.index(n)+1]:
                    i += 1
                    continue
                else:
                    print(n)
                    flag = False
            else:
                print(n)

ejemplo = [1, 1, 3, 3, 4, 5, 5, 6, 6, 7, 7]
numNoMult(ejemplo)

'''
 if n == listaNumDobles[listaNumDobles.index(n)+1]:
IndexError: list index out of range
'''
#ejemplo2 = [1, 1, 3, 3, 4, 4, 5, 5, 6, 6, 7]
#numNoMult(ejemplo2)

print("-"*50)
#3
#Escribe una función que cuente el número de vocales en una cadena dada.
def vocales(st):
    counter = 0
    l = list(st)
    for letter in l:
        if letter == 'a':
            counter += 1
        elif letter == 'e':
            counter += 1
        elif letter == 'i':
            counter += 1
        elif letter == 'o':
            counter += 1
        elif letter == 'u':
            counter += 1
        else:
            continue
    print("{0} tiene {1} vocales".format(st,counter))
    
s = "murcielago"
s2 = "hannah"
vocales(s)
vocales(s2)


print("-"*50)
#4
'''
Elabora un programa que me permita realizar la suma de dos matrices de 3x3. 
Cada uno de los elementos de la matriz deberá ser ingresado por el usuario. 
Una matriz en Python puede implementarse con listas dentro de listas.
'''
def convert(string): 
    li = list(string.split(" ")) 
    return li 

def sumaMatrices(lista1, lista2):
    suma = [[0,0,0],[0,0,0],[0,0,0]]
    #Renglones
    for r in range(len(lista1)):
        #Columnas
        for x in range(len(lista1[0])):
            suma[r][x] = int(lista1[r][x]) + int(lista2[r][x])
    print(suma)

    '''
    Primero se mete a la lista 
    O sea hace la suma en los índices en este orden:
    
    0,0
    0,1
    0,2

    1,0
    1,1
    1,2

    2,0
    2,1
    2,2

    '''


#Matriz 1
mat1 = []
print("Primera matriz\n")
c1 = convert(input("Ingrese la primer fila (Cada numero separado por un espacio): "))
c2 = convert(input("Ingrese la segunda fila (Cada numero separado por un espacio): "))
c3 = convert(input("Ingrese la tercer fila (Cada numero separado por un espacio): "))
mat1.append(c1)
mat1.append(c2)
mat1.append(c3)

#Matriz 2
mat2 = []
print("\nSegunda matriz\n")
c1 = convert(input("Ingrese la primer fila (Cada numero separado por un espacio): "))
c2 = convert(input("Ingrese la segunda fila (Cada numero separado por un espacio): "))
c3 = convert(input("Ingrese la tercer fila (Cada numero separado por un espacio): "))
mat2.append(c1)
mat2.append(c2)
mat2.append(c3)

print(mat1)
print(mat2)


sumaMatrices(mat1, mat2)

print("-"*50)
#5
'''
Dada una lista de cadenas de diferentes longitudes, crear una función que tome 
como entrada dicha lista y la devuelva ordenada de la cadena más pequeña a la 
más larga.
'''
def ordena(lista): 
    lista.sort(key=len) 
    return lista

listaEj = ["uno", "abecedario", "hannah"]
print(listaEj)
print(ordena(listaEj))

print("-"*50)
#6
'''
Elabora un programa que sea capaz de calcular el IMC (Índice de masa corporal) 
de una persona. Los datos deberán ser ingresados por el usuario.
'''
def calc_imc(w,h):
    imc = w/((h**2))
    print(str(imc))

peso = float(input("Ingresa tu peso (en kg): "))
altura = float(input("Ingresa tu altura(en metros): "))
calc_imc(peso, altura)

print("-"*50)
#7
'''
Con ayuda de diccionarios y listas, elabora un programa que simule una agenda 
de contactos. El programa debe preguntar al usuario si desea agregar un nuevo 
contacto a su agenda; si el usuario responde que sí, deberá pedir datos como 
“nombre” y “teléfono”; en caso contrario deberá mostrar todos los usuarios 
agregados en la agenda y termina la ejecución del programa.
'''
agenda = []
while True:
    opc = input("Desea agregar un contacto a la agenda: ")
    if (opc == "si"):
        nombre = input("Ingrese el nombre: ")
        telefono = int(input("Ingrese el telefono: "))
        nuevo_contacto = {telefono: nombre}
        agenda.append(nuevo_contacto)

    else:
        print(agenda)
        False
        break
