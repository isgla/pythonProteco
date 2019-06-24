#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 10:50:35 2019

@author: isgla
"""

import matplotlib.pyplot as plt
import scipy as sp

#FIGURA 1----------------------------
plt.figure(1)

#Del 1 al 10 en 100 puntos
ejeX = sp.linspace(1,10,100)

plt.ylabel('Mi función coseno')
plt.title('Figura 1')

#linespace, funcion (que es y),estilo (estilos de linea y marcadores)
y = sp.cos(ejeX)
plt.plot(ejeX, y, 'c--')

#FIGURA 2----------------------------
#Cada figure es una ventana
plt.figure(2)
plt.title('Figura 2')
#Si pones ejeX2 te sale una gráfica partida
ejeX2 = sp.linspace(10,50,20)
g = sp.sin(ejeX2)
plt.xlabel('eje x')
plt.ylabel('Mi función seno')
plt.plot(ejeX2, g, 'r--')

#FIGURA 3----------------------------
plt.figure(3)
plt.title('Figura 3')
with plt.style.context(('dark_background')):
    plt.plot(ejeX2, g, 'r-o')
    
#plt.style.use(['dark_background', 'presentation'])


plt.show()
