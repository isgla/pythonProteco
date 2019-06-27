#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 09:35:52 2019

@author: cur01alu13
"""
"""
from sympy import *
#Forzar tipos de datos
entero = 5
transformacion = Float(entero)
print(transformacion)

fraccion = Rational(1,2)
fraccion2 = Rational(3,8)
entreCero = Rational(4,0)
suma = fraccion + fraccion2
print(suma)
print(entreCero)"""

from sympy import pi, E, oo, limit, cos
radio = 5
#Sin el evalf la operación queda expresada únicamente
area = pow((pi.evalf() * radio),2)
print(area)
#5**3
print(E.evalf())
print(oo.evalf())

#---------------VARIABLES SIMBÓlICAS-------------------
#a
#Símbolos
x = Symbol('x')
y = Symbol('y')
print(x)
print(y)
#Muchos símbolos a la vez
a,b,c = symbols('a,b,c')
print(a,b,c)
variables = var('q:w')
print(variables)
#Ecuación general
ecuacion = x + y
print(ecuacion)
#Solución particular
sol_par = ecuacion.subs(x,3)
print(sol_par)
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
e = (x**2) - 5
print(solve(e))
#Cálculo de lìmites
#función, variable respecto a..., valor al que tiende
print(limit(cos(x)/x, x,0))
print(limit(sin(x)/x, x,0))
#Calculando integral
#Función, (variable respecto a, limite superior, limite inferior)
print(integrate(x**3,(x,-1,1)))





















