# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt

x = [-1,0,1]
y = [2,1,3]
l = lagrange(x,y)
print(l)

#Solución particular
print(l(1/2))
plt.plot(x,y,'o')
plt.show()

