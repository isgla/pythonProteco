#Recursividad

#Factorial iterativo
"""
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

print(factorialRec(4))
"""

def fibo(n):
	if n == 1 or n == 2:
		return 1
	return fibo(n-1)+fibo(n-2)






