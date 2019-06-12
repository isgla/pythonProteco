#Diccionarios
x = {}
x['red'] = "El color rojo"
x['blue'] = "El color azul"
print(x)

#Para imprimir en pantalla "el color rojo"
print(x["red"])

#Llenando diccionario en una sóla línea de código
y = {"red":"el color rojo", "blue":"El color azul"}
print(y)

#Diccionarios de varios tipos de datos
y = {"uno": 1, 2: "dos", 2.5: "numero flotante", "lista": [2,3,4,"hola"],
(1,2,3): "una tupla"}
print(y[(1,2,3)])
print(y[2.5])


"""
[2,"hola"]: "prueba"
No se puede usar una lista como llave porque es mutable, entonces la llave, 
no podría hacer su hash
print(y[[2,"hola"]])

Por lo tanto sólo puedo usar cadenas, números, tuplas comos llave
"""

#Alterando el valor
y["lista"] = "mundo"
print(y)

#Recuperando llaves
claves = y.keys()
print(claves)
aux = list(claves)
print(aux)

#Recuperando los valores
valores = y.values()
print(valores)
#Conviertes los valores a una lista
aux2 = list(valores)
print(aux2)

#Buscando valores
#Regresa True si lo encuentra
print("dos" in valores)

print("-"*80)
#Borra la llave, y borra el elemento de esa llave
del y["uno"]
print(y)

del y

"""
del y
print(y)
Traceback (most recent call last):
  File "diccionarios.py", line 56, in <module>
    print(y)
NameError: name 'y' is not defined
"""



