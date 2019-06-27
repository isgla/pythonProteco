import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
x= [-1,0,1]
y=[2,1,3]
p = lagrange(x,y)
print(p)
#Si quiero evaluar el polinomio:
x0 = 1/2
sol_particular = p(x0)
print("""Resultado del polinomio evaluado en
2: """, sol_particular)
#Gráfica
#plt.figure(1)
#plt.plot(1/2,sol_particular,'o')
plt.plot(x,y,'o')
plt.show()