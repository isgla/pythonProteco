#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 09:37:00 2019

@author: cur01alu30
"""

from sklearn.datasets import load_iris
from sklearn import tree
import numpy

iris = load_iris()

#Obteniendo datos que se usarán como prueba
#Setosa -> 0
# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
prueba_target = iris.target[0]
# ['setosa' 'versicolor' 'virginica']
prueba_data = iris.data[0]

#De que conjunto vas a borras y cuales osn los indices del conjunto que vas a borrar
#Target - lo que quiero obtener
target = numpy.delete(iris.target,[0,50,100])
data = numpy.delete(iris.data, [0,50,100], axis=0)

clasificador = tree.DecisionTreeClassifier()

clasificador = clasificador.fit(data, target)

print("Datos de prueba")
print(prueba_target)
print(prueba_data)

print(clasificador.predict([prueba_data])) #El resultado es 0 entonces es una setosa

print(clasificador.predict([[4,2,1,1.5]]))
