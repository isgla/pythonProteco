#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 08:45:49 2019

@author: isgla
"""

import numpy as np

lista = [1,2,4]
tupla = (1,2,3)
vector = np.array([2,3,4,5])
vector2 = np.array([6,7,8,9])

print(lista)
print(tupla)
print(vector)

#Suma de vectores
suma = vector + vector2
print(suma)

#Producto punto
productoPunto = vector.dot(vector2)
print(productoPunto)

#Creando matrices con el método array
m1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
m2 = np.array([[1],[2],[3]])

print(m1)
print(m2)

#Multiplicación de matrices usando array y método dot
print(m1.dot(m2))

#Array con un rango de valores
arr1 = np.arange(10)
print(arr1)

arr2 = np.arange(2,20)
print("\n", arr2)

arr3 = np.arange(4,20,3)
print("\n",arr3)


#Arreglos especiales
unos = np.ones((2,2))
print(unos)

ceros = np.zeros((3,5))
print(ceros)

#Del 0 al 3 en 9 puntos
lins = np.linspace(0,3,9)
print(lins)

#Imprimiría cuartos
lins = np.linspace(0,1,6)
print(lins)
#[0.  0.2 0.4 0.6 0.8 1. ]

#Matriz diagonal
diagonal = np.eye(3)
print(diagonal)

#----------MATRIX----------
#Transpuesta (Renglones <=> Columnas)
matriz1 = np.matrix([[1,3,-5],[8,9,1+10j]])
print(matriz1)
print(matriz1.T)

#Hermitiana
print(matriz1.H)

#Inversa
print(matriz1.I)

#Multiplicación
m5 = np.matrix([[5,5,5],[6,6,6]]) #2x3
m6 = np.matrix([[4,4],[7,7],[8,8]]) #3x2
print(m5*m6)

m5 = np.matrix([[5,5,5],[6,6,6]]) #2x3
m6 = np.matrix([[4,4],[7,7]]) #3x2

try:
    print(m5*m6)
except ValueError:
    print("No cumple con la regla de multiplicación de matrices")


