#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 09:27:04 2019

@author: isgla
"""

from sklearn.datasets import load_iris

iris = load_iris()

print(iris.feature_names)
print(iris.target_names)

print(iris.data[0]])
print(iris.target[0])

# 0 -> Setosa
# 1 -> Versicolor
# 2 -> Virginica

for i in range(len(iris.target)):
    print("Dato {0}: label {1}, features {2}".format(i, iris.target[i], iris.data[i]))

