#Recursividad

#Factorial iterativo
def factorial(num):
	fact = 1
	for x in range(1,num+1):
		fact *= x
	return fact

print(factorial(3))

#Factorial recursivo
def factorialRec(num):
	if num==0 or num==1:
		return 1
	else:
		return num*factorialRec(num-1)

print(factorial(4))

"""
Ejemplo

Factorial 4

¿Es 0 o 1? No
=> 4*factorialRec(3)

¿Es 0 o 1? No
=> 4*3*factorialRec(2)

¿Es 0 o 1? No
=> 4*3*2*factorialRec(1)

¿Es 0 o 1? Si
=> 4*3*2*1
"""