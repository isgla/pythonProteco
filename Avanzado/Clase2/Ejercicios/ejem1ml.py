#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 09:04:37 2019

@author: isgla
"""

#Arboles de decisión - Supervisado
from sklearn import tree

#Datos del clasificador

#Características (Features)
"""
Peso  Textura   Label
150   Rugosa    Naranja
170   Rugosa    Naranja
140   Lisa      Manzana
130   Lisa      Manzana

0 -> Rugosa
1 -> Lisa
"""

features = [[150,0],[170,0],[140,1],[130,1]]
labels = ['Naranja', 'Naranja', 'Manzana', 'Manzana']

#Crear nuestro árbol
clasificador = tree.DecisionTreeClassifier()

#El algoritmo de aprendizaje incluido en el clasificador se llama 'fit'
clasificador = clasificador.fit(features, labels)

#Realizar predicciones
#Quiero que me digas que pesa si una fruta pesa 160 y tiene una textura rugosa
print(clasificador.predict([[160, 0]]))