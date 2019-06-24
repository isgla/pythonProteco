#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 09:37:03 2019

@author: isgla
"""
#Importamos constantes
from sympy import pi, E, oo, cos
#E es número de euler
#oo es infinito

radio = 5
#Sin el evalf la operación queda expresada únicamente
area = pow((pi.evalf() * radio),2) #por es potencia
print(area)

print(E.evalf())
print(oo.evalf())

#-------VARIABLES SIMBÓLICAS-------
#a
#Símbolos 
x = Symbol('x')
y = Symbol('y')
print(x)
print(y)
#Muchos símbolos a la vez
a, b, c = symbols('a,b,•')
print(a,b,c)

#Regresa una tupla (q, r, s, t, u, v, w) 
variables = var('q:w')
print(variables)

#Ecuacion general
ecuacion = x + y
print(ecuacion)
#x + y

#Solución particular
sol_par = ecuacion.subs(x,3)
print(sol_par)
#y + 3

#Sustituyendo otros símbolos
sol = ecuacion.subs(x,y)
print(sol)

#Múltiples sustituciones
p = Symbol('p')
ecuacion2 = x*2 + 5*y - p
print(ecuacion2)
aux = ecuacion2.subs([(x,1),(y,5),(p,x)])
print(aux)

#Solución de ecuaciones
e = (x**2) - 5*y
print(solve(e))

#Cálculo de límites
#función, variable respecto a ..., valor al que tiende
print(limit(cos(x)/ x, x, 0))
print(limit(sin(x)/ x, x, 0))

#Calculando integral
#Función, (variable respecto a, límite superior, límite inferior)
print(integrate(x**3,(x,-1,1)))

"""
#Forzar tipos de datos
entero = 5
transformacion = Float(entero)
print(transformacion)

fraccion = Rational(1,2) #1/2
fraccion2 = Rational(3,8) #3/8
entreCero = Rational(4,0) #Entre cero me da infinito (zoo = complex infinity)
suma = fraccion + fraccion2
print(suma)
print(entreCero)
"""