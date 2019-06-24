#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:34:43 2019

@author: cur01alu46
"""
#FIGURA 1-----------------

import matplotlib.pyplot as plt
import scipy as sp

#Cada figure es una ventana.
plt.figure(1)

ejeX = sp.linspace(1,10,100)
y = sp.cos(ejeX)
plt.title('Figura 1')
plt.xlabel('eje x')
plt.ylabel('Mi función coseno')
#x = sm.Symbol('x')
#y es la función cos
#'' es donde decoramos
plt.plot(ejeX,y,'m--')

#FIGURA 2------------------

#Cada figure es una ventana.
#Si le quitamos el figure se hace en la misma ventana.
plt.figure(2)
#linspace : divide el eje
ejeX2 = sp.linspace(10,50,20)
g = sp.sin(ejeX2)
plt.xlabel('eje x')
plt.ylabel('Mi función seno')
plt.title('Figura 2')
plt.plot(ejeX2,g,'r--')

#FIGURA 3-------------
plt.figure(3)
with plt.style.context(('dark_background')):
    plt.plot(ejeX2, g , 'r-o')


plt.show() 


