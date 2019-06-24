#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:35:35 2019

@author: cur01alu46
"""

import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_excel('tabla1.xlsx', 'Hoja 1')
print(df)

#Conocer datos de una sola columna
aux = df['Numero']
aux2 = df['Edad']

plt.plot(aux, aux2, 'ro')
plt.show()