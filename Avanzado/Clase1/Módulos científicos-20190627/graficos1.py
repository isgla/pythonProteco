#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 10:48:03 2019

@author: cur01alu13
"""
import matplotlib.pyplot as plt
import scipy as sp
#CADA FIGURE ES UNA VENTANA
#FIGURA 1---------
plt.figure(1)
ejeX = sp.linspace(1,10,100)
y = sp.cos(ejeX)
plt.title('Figura 1')
plt.xlabel('eje x')
plt.ylabel('Mi función coseno')
plt.plot(ejeX, y, 'bo')
#FIGURA 2---------
plt.figure(2)
ejeX2 = sp.linspace(10, 50, 20)
g = sp.sin(ejeX2)
plt.xlabel('eje x')
plt.ylabel('Mi función seno')
plt.title('Figura 2')
plt.plot(ejeX2, g, 'r--')

#FIGURA 3
plt.figure(3)
with plt.style.context(('dark_background')):
    plt.plot(ejeX2, g, 'r-o')


plt.show()


